# credit: https://github.com/AI4Bharat/IndicXlit

import os
import enum
import traceback
import re
import ast
import math
import time
import logging

from argparse import Namespace
from collections import namedtuple
import zipfile
from pydload import dload

from fairseq import checkpoint_utils, options, tasks, utils
from fairseq.dataclass.utils import convert_namespace_to_omegaconf
from fairseq.token_generation_constraints import pack_constraints, unpack_constraints
from fairseq_cli.generate import get_symbols_to_strip_from_output

logging.disable()

class XlitError(enum.Enum):
    lang_err = "Unsupported langauge ID requested ;( Please check available languages."
    string_err = "String passed is incompatable ;("
    internal_err = "Internal crash ;("
    unknown_err = "Unknown Failure"
    loading_err = "Loading failed ;( Check if metadata/paths are correctly configured."

F_DIR = os.path.dirname(os.path.realpath(__file__))
SUPPORTED_INDIC_LANGS = {"as", "bn", "brx", "gom", "gu", "hi", "kn", "ks", "mai", "ml", "mni", "mr", "ne", "or", "pa", "sa", "sd", "si", "ta", "te", "ur"}

MODEL_DOWNLOAD_URL = 'https://storage.googleapis.com/indic-xlit-public/final_model/indicxlit-en-indic-v1.0.zip'
XLIT_VERSION = "v1.0" # If model/dict is changed on the storage, do not forget to change this variable in-order to force-download new assets

MODEL_FILE = 'transformer/indicxlit.pt'
CHARS_FOLDER = 'corpus-bin'


#################################### Creating Transliterator and input batches #############################

Batch = namedtuple("Batch", "ids src_tokens src_lengths constraints")
Translation = namedtuple("Translation", "src_str hypos pos_scores alignments")

def make_batches(lines, cfg, task, max_positions, encode_fn):
    def encode_fn_target(x):
        return encode_fn(x)


    if cfg.generation.constraints:
        # Strip (tab-delimited) contraints, if present, from input lines,
        # store them in batch_constraints
        batch_constraints = [list() for _ in lines]
        for i, line in enumerate(lines):
            if "\t" in line:
                lines[i], *batch_constraints[i] = line.split("\t")

        # Convert each List[str] to List[Tensor]
        for i, constraint_list in enumerate(batch_constraints):
            batch_constraints[i] = [
                task.target_dictionary.encode_line(
                    encode_fn_target(constraint),
                    append_eos=False,
                    add_if_not_exist=False,
                )
                for constraint in constraint_list
            ]

    if cfg.generation.constraints:
        constraints_tensor = pack_constraints(batch_constraints)
    else:
        constraints_tensor = None

    tokens, lengths = task.get_interactive_tokens_and_lengths(lines, encode_fn)

    itr = task.get_batch_iterator(
        dataset=task.build_dataset_for_inference(
            tokens, lengths, constraints=constraints_tensor
        ),
        max_tokens=cfg.dataset.max_tokens,
        max_sentences=cfg.dataset.batch_size,
        max_positions=max_positions,
        ignore_invalid_inputs=cfg.dataset.skip_invalid_size_inputs_valid_test,
    ).next_epoch_itr(shuffle=False)
    for batch in itr:
        ids = batch["id"]
        src_tokens = batch["net_input"]["src_tokens"]
        src_lengths = batch["net_input"]["src_lengths"]
        constraints = batch.get("constraints", None)

        yield Batch(
            ids=ids,
            src_tokens=src_tokens,
            src_lengths=src_lengths,
            constraints=constraints,
        )

class Transliterator:
    def __init__(self, data_bin_dir, model_checkpoint_path, beam, batch_size = 32):
        self.parser = options.get_interactive_generation_parser()
        # buffer_size is currently not used but we just initialize it to batch
        # size + 1 to avoid any assertion errors.
        
        self.parser.set_defaults(
            path = model_checkpoint_path,
            num_wokers = -1,
            batch_size = batch_size,
            buffer_size = batch_size + 1,
            task = "translation_multi_simple_epoch",
            beam = beam
        )
        
        self.args = options.parse_args_and_arch(self.parser, input_args = [data_bin_dir] )
        self.args.skip_invalid_size_inputs_valid_test = False
        self.args.lang_pairs = ','.join(["en-"+lang for lang in SUPPORTED_INDIC_LANGS])
        self.cfg = convert_namespace_to_omegaconf(self.args)

        if isinstance(self.cfg, Namespace):
            self.cfg = convert_namespace_to_omegaconf(self.cfg)

        self.total_translate_time = 0

        utils.import_user_module(self.cfg.common)

        if self.cfg.interactive.buffer_size < 1:
            self.cfg.interactive.buffer_size = 1
        if self.cfg.dataset.max_tokens is None and self.cfg.dataset.batch_size is None:
            self.cfg.dataset.batch_size = 1

        assert (
            not self.cfg.generation.sampling or self.cfg.generation.nbest == self.cfg.generation.beam
        ), "--sampling requires --nbest to be equal to --beam"
        assert (
            not self.cfg.dataset.batch_size
            or self.cfg.dataset.batch_size <= self.cfg.interactive.buffer_size
        ), "--batch-size cannot be larger than --buffer-size"


        # self.use_cuda = torch.cuda.is_available() and not self.cfg.common.cpu
        self.use_cuda = False
        self.task = tasks.setup_task(self.cfg.task)

        # Load ensemble
        overrides = ast.literal_eval(self.cfg.common_eval.model_overrides)
        self.models, _model_args = checkpoint_utils.load_model_ensemble(
            utils.split_paths(self.cfg.common_eval.path),
            arg_overrides=overrides,
            task=self.task,
            suffix=self.cfg.checkpoint.checkpoint_suffix,
            strict=(self.cfg.checkpoint.checkpoint_shard_count == 1),
            num_shards=self.cfg.checkpoint.checkpoint_shard_count,
        )

        # Set dictionaries
        self.src_dict = self.task.source_dictionary
        self.tgt_dict = self.task.target_dictionary


        # Optimize ensemble for generation
        for model in self.models:
            if model is None:
                continue
            if self.cfg.common.fp16:
                model.half()
            if self.use_cuda and not self.cfg.distributed_training.pipeline_model_parallel:
                model.cuda()
            model.prepare_for_inference_(self.cfg)

        # Initialize generator
        self.generator = self.task.build_generator(self.models, self.cfg.generation)

        # Handle tokenization and BPE
        self.tokenizer = self.task.build_tokenizer(self.cfg.tokenizer)
        self.bpe = self.task.build_bpe(self.cfg.bpe)

        # Load alignment dictionary for unknown word replacement
        # (None if no unknown word replacement, empty if no path to align dictionary)
        self.align_dict = utils.load_align_dict(self.cfg.generation.replace_unk)

        self.max_positions = utils.resolve_max_positions(
            self.task.max_positions(), *[model.max_positions() for model in self.models]
        )

    def encode_fn(self, x):
        if self.tokenizer is not None:
            x = self.tokenizer.encode(x)
        if self.bpe is not None:
            x = self.bpe.encode(x)
        return x

    def decode_fn(self, x):
        if self.bpe is not None:
            x = self.bpe.decode(x)
        if self.tokenizer is not None:
            x = self.tokenizer.decode(x)
        return x

    def translate(self, inputs, nbest=1):

        start_id = 0
        results = []
        for batch in make_batches(inputs, self.cfg, self.task, self.max_positions, self.encode_fn):
            bsz = batch.src_tokens.size(0)
            src_tokens = batch.src_tokens
            src_lengths = batch.src_lengths
            constraints = batch.constraints
            if self.use_cuda:
                src_tokens = src_tokens.cuda()
                src_lengths = src_lengths.cuda()
                if constraints is not None:
                    constraints = constraints.cuda()

            sample = {
                "net_input": {
                    "src_tokens": src_tokens,
                    "src_lengths": src_lengths,
                },
            }

            translate_start_time = time.time()
            translations = self.task.inference_step(
                self.generator, self.models, sample, constraints=constraints
            )
            translate_time = time.time() - translate_start_time
            self.total_translate_time += translate_time

            list_constraints = [[] for _ in range(bsz)]
            if self.cfg.generation.constraints:
                list_constraints = [unpack_constraints(c) for c in constraints]
            for i, (id, hypos) in enumerate(zip(batch.ids.tolist(), translations)):
                src_tokens_i = utils.strip_pad(src_tokens[i], self.tgt_dict.pad())
                constraints = list_constraints[i]
                results.append(
                    (
                        start_id + id,
                        src_tokens_i,
                        hypos,
                        {
                            "constraints": constraints,
                            "time": translate_time / len(translations),
                        },
                    )
                )

        # sort output to match input order
        result_str = ""
        for id_, src_tokens, hypos, info in sorted(results, key=lambda x: x[0]):

            src_str = ""
            if self.src_dict is not None:
                src_str = self.src_dict.string(src_tokens, self.cfg.common_eval.post_process)
                result_str += "S-{}\t{}".format(id_, src_str) + '\n'
                result_str += "W-{}\t{:.3f}\tseconds".format(id_, info["time"]) + '\n'

                for constraint in info["constraints"]:
                    result_str += "C-{}\t{}".format(
                            id_,
                            self.tgt_dict.string(constraint, self.cfg.common_eval.post_process),
                        ) + '\n'

            # Process top predictions
            for hypo in hypos[: min(len(hypos), nbest)]:
                hypo_tokens, hypo_str, alignment = utils.post_process_prediction(
                    hypo_tokens=hypo["tokens"].int().cpu(),
                    src_str=src_str,
                    alignment=hypo["alignment"],
                    align_dict=self.align_dict,
                    tgt_dict=self.tgt_dict,
                    remove_bpe=self.cfg.common_eval.post_process,
                    extra_symbols_to_ignore=get_symbols_to_strip_from_output(self.generator),
                )
                detok_hypo_str = self.decode_fn(hypo_str)
                score = hypo["score"] / math.log(2)  # convert to base 2
                result_str += "H-{}\t{}\t{}".format(id_, score, hypo_str) + '\n'
                result_str += "D-{}\t{}\t{}".format(id_, score, detok_hypo_str) + '\n'
                
                result_str += "P-{}\t{}".format(
                        id_,
                        " ".join(
                            map(
                                lambda x: "{:.4f}".format(x),
                                # convert from base e to base 2
                                hypo["positional_scores"].div_(math.log(2)).tolist(),
                            )
                        ),
                    ) + '\n'

                if self.cfg.generation.print_alignment:
                    alignment_str = " ".join(
                        ["{}-{}".format(src, tgt) for src, tgt in alignment]
                    )
                    result_str += "A-{}\t{}".format(id_, alignment_str) + '\n'
        return result_str

#######################################################################################################

############################# Creating Engine for Transliterator ######################################


def is_folder_writable(folder):
    try:
        os.makedirs(folder, exist_ok=True)
        tmp_file = os.path.join(folder, '.write_test')
        with open(tmp_file, 'w') as f:
            f.write('Permission Check')
        os.remove(tmp_file)
        return True
    except:
        return False

def is_directory_writable(path):
    if os.name == 'nt':
        return is_folder_writable(path)
    return os.access(path, os.W_OK | os.X_OK)


class Transliteration():
    """
    For Managing the top level tasks and applications of transliteration
    """

    def __init__(self,  beam_width=4):
        self.langs = {"ne"}
        if is_directory_writable(F_DIR):
            models_path = os.path.join(F_DIR, 'models')
        else:
            user_home = os.path.expanduser("~")
            models_path = os.path.join(user_home, '.AI4Bharat_Xlit_Models')
        models_path = os.path.join(models_path, XLIT_VERSION)

        os.makedirs(models_path, exist_ok=True)
        self.download_models(models_path)

        # initialize the model
        self.transliterator = Transliterator(
            os.path.join(models_path, CHARS_FOLDER), os.path.join(models_path, MODEL_FILE), beam_width, batch_size = 32
        )
        


    def download_models(self, models_path):
        '''
        Download models from bucket
        '''

        model_file_path = os.path.join(models_path, MODEL_FILE)
        if not os.path.isfile(model_file_path):
            print('Downloading Multilingual model for transliteration')
            remote_url = MODEL_DOWNLOAD_URL
            downloaded_zip_path = os.path.join(models_path, 'model.zip')
            
            dload(url=remote_url, save_to_path=downloaded_zip_path, max_time=None)

            if not os.path.isfile(downloaded_zip_path):
                exit(f'ERROR: Unable to download model from {remote_url} into {models_path}')

            with zipfile.ZipFile(downloaded_zip_path, 'r') as zip_ref:
                zip_ref.extractall(models_path)

            if os.path.isfile(model_file_path):
                os.remove(downloaded_zip_path)
            else:
                exit(f'ERROR: Unable to find models in {models_path} after download')
            
            print("Models downloaded to:", models_path)
        return


    def pre_process(self, words, lang_code):
        # small caps 
        words = [word.lower() for word in words]
        # convert the word into sentence which contains space separated chars
        words = [' '.join(list(word)) for word in words]
        # adding language token
        words = ['__'+ lang_code +'__ ' + word for word in words]
        return words

    def post_process(self, translation_str, target_lang):
        lines = translation_str.split('\n')

        list_s = [line for line in lines if 'S-' in line]
        list_h = [line for line in lines if 'H-' in line]

        list_s.sort(key = lambda x: int(x.split('\t')[0].split('-')[1]) )
        list_h.sort(key = lambda x: int(x.split('\t')[0].split('-')[1]) )

        res_dict = {}
        for s in list_s:
            s_id = int(s.split('\t')[0].split('-')[1])
            res_dict[s_id] = { 'S' : s.split('\t')[1] }
            
            res_dict[s_id]['H'] = []
            for h in list_h:
                h_id = int(h.split('\t')[0].split('-')[1])
                if s_id == h_id:
                    res_dict[s_id]['H'].append( ( h.split('\t')[2], pow(2,float(h.split('\t')[1])) ) )

        for r in res_dict.keys():
            res_dict[r]['H'].sort(key = lambda x : float(x[1]) ,reverse =True)
        
        result_dict = {}
        for i in res_dict.keys():            
            result_dict[res_dict[i]['S']] = {}
            for j in range(len(res_dict[i]['H'])):
                 result_dict[res_dict[i]['S']][res_dict[i]['H'][j][0]] = res_dict[i]['H'][j][1]
        
        
        transliterated_word_list = []
        for i in res_dict.keys():
            for j in range(len(res_dict[i]['H'])):
                transliterated_word_list.append( res_dict[i]['H'][j][0] )

        transliterated_word_list = [''.join(word.split(' ')) for word in transliterated_word_list]
        return transliterated_word_list

    def translit_word(self, word, topk=4):
        # exit if invalid inputs
        if not word:
            print("error : Please insert valid inputs : pass one word")
            return
        words = [word, ]

        # check if there is non-english characters
        pattern = '[^a-zA-Z]'   
        words = [ word for word in words if not re.compile(pattern).search(word) ]
        if not words:
            print("error : Please insert valid inputs : only pass english characters ")
            return

        try:
            perprcossed_words = self.pre_process(words, "ne")
            translation_str = self.transliterator.translate(perprcossed_words, nbest=topk)
            transliterated_word_list = self.post_process(translation_str, "ne")

        except Exception as error:
                print("XlitError:", traceback.format_exc())
                print(XlitError.internal_err.value)
                return XlitError.internal_err

        return transliterated_word_list
        

    def translit_sentence(self, eng_sentence):
        if not eng_sentence:
            return eng_sentence
        
        eng_sentence = eng_sentence.lower()
        matches = re.findall("[a-zA-Z]+", eng_sentence)

        try:
            out_str = eng_sentence
            for match in matches:
                result = self.translit_word(match, topk=1)[0]
                out_str = re.sub(match, result, out_str, 1)
            return out_str

        except Exception as error:
            print("XlitError:", traceback.format_exc())
            print(XlitError.internal_err.value)
            return XlitError.internal_err