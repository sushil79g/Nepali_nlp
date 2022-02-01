from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


class LanguageTranslation:
    def __init__(self) -> None:
        self.model = MBartForConditionalGeneration.from_pretrained(
            "facebook/mbart-large-50-many-to-many-mmt"
        )
        self.tokenizer = MBart50TokenizerFast.from_pretrained(
            "facebook/mbart-large-50-many-to-many-mmt"
        )

    def to_nepali(self, text):
        self.tokenizer.src_lang = "en_XX"
        encoded_foreign = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(
            **encoded_foreign,
            forced_bos_token_id=self.tokenizer.lang_code_to_id["ne_NP"]
        )
        converted = self.tokenizer.batch_decode(
            generated_tokens, skip_special_tokens=True
        )
        return converted

    def to_english(self, text):
        self.tokenizer.src_lang = "ne_NP"
        encode_nepali = self.tokenizer(text, return_tensors="pt")
        generated_tokens = self.model.generate(
            **encode_nepali, forced_bos_token_id=self.tokenizer.lang_code_to_id["en_XX"]
        )
        converted = self.tokenizer.batch_decode(
            generated_tokens, skip_special_tokens=True
        )
        return converted
