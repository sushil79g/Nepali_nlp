from tokenize import Tokenizer

class NgramGenerator(Tokenizer):

    def __init__(self,n_gram):
        self.n_gram = n_gram

    def generate_n_gram(self,token_text):
        """This function generate ngram token list
        
            Arguments:
                sentence {list} -- list of tokenized text
                n_gram {int} -- value of n-gram
        
            Returns:
                list --  multi array list of n-gram tokenized words
            """

        n_gram_wordlist=[]
        for idx in range(len(token_text)-self.n_gram+1):
            n_gram_wordlist.append(token_text[idx:idx+self.n_gram])
        return n_gram_wordlist
