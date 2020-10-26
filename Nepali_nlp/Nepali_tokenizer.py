import os
import sys 
sys.path.append('..')
import string

import tensorflow as tf
import sentencepiece as spm

class Tokenizer:
    def __init__(self):
        self.this_dir, self.this_file = os.path.split(__file__)

    def sentence_tokenize(self, text):
        """This function tokenize the sentences
        
        Arguments:
            text {string} -- Sentences you want to tokenize
        
        Returns:
            sentence {list} -- tokenized sentence in list
        """
        sentences = text.strip().split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences

    def word_tokenize(self, sentence, new_punctuation=[]):
        """This function tokenize with respect to word
        
        Arguments:
            sentence {string} -- sentence you want to tokenize
            new_punctuation {list} -- more punctutaion for tokenizing  default ['।',',',';','?','!','—','-']
        
        Returns:
            list -- tokenized words
        """
        punctuations = ['।', ',', ';', '?', '!', '—', '-', '.']
        if new_punctuation:
            punctuations = set(punctuations + new_punctuation)

        for punct in punctuations:
            sentence = ' '.join(sentence.split(punct))

        return sentence.split()

    def character_tokenize(self, word):
        """ Returns the tokenization in character level.
        
        Arguments:
            word {string} -- word to be tokenized in character level.
        
        Returns:
            [list] -- list of characters.
        """
        try:
            import icu

        except:
            print("please install PyICU")
        
        temp_ = icu.BreakIterator.createCharacterInstance(icu.Locale())
        temp_.setText(word)
        char = []
        i = 0
        for j in temp_:
            s = word[i:j]
            char.append(s)
            i = j

        return char

    def sentencepeice_tokenize(self, text):
        """unsupervised way of tokenizing the text using google sentencepiece library. More info at https://github.com/google/sentencepiece

        Args:
            text (string): Text in Nepali language
        
        Returns:
            list: tokenized words.
        """
        try:
            model = tf.gfile.Gfile(os.path.join(self.this_dir, "local_dataset", "m_bpe.model"), "rb").read() #tf version 1
        except:
            model = tf.io.gfile.GFile(os.path.join(self.this_dir, "local_dataset", "m_bpe.model"), "rb").read() #tf version 2
        sp = spm.SentencePieceProcessor()
        sp.load_from_serialized_proto(model)
        return sp.encode_as_pieces(text)


    def __str__(self):
        return "Helps to tokenize content written in Nepali language."
