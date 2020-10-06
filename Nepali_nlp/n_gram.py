import sys
sys.path.append('..')

from .Nepali_tokenizer import Tokenizer

class NgramGenerator(Tokenizer):

    def __init__(self, n_gram):
        self.n_gram = n_gram

    def generate_n_gram(self, token_text):
        """This function generate ngram token list
        
            Arguments:
                sentence {list} -- list of tokenized text
                n_gram {int} -- value of n-gram
        
            Returns:
                list --  multi array list of n-gram tokenized words
            """

        n_gram_wordlist = []
        for idx in range(len(token_text) - self.n_gram + 1):
            n_gram_wordlist.append(token_text[idx:idx + self.n_gram])
        return n_gram_wordlist

# --------------------------------Test Case------------------------------------------------

# data = "तिमीले सुन्या यो कुरा हो, मैले सुन्या को कुरा हो ,तिम्रो हाम्रो सम्बन्ध को हल्ला चल्या को कुरा हो ,झ्याम्म झ्याम्म।"
# one_gram = NgramGenerator(1)
# two_gram = NgramGenerator(2)
# three_gram = NgramGenerator(3)

# print(one_gram.generate_n_gram(one_gram.word_tokenize(data)))
# print(two_gram.generate_n_gram(two_gram.word_tokenize(data)))
# print(three_gram.generate_n_gram(three_gram.word_tokenize(data)))
