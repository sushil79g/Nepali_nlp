from tokenize import Tokenizer

token = Tokenizer()

def generate_n_gram(text, n_gram):
    """This function generate ngram token list
        
        Arguments:
            sentence {string} -- sentence from which N-gram should be generated
            n_gram {int} -- value of n-gram
        
        Returns:
            list -- list of n-gram words
        """
    token =  Tokenizer()
    word_token  = token.word_tokenize(text)
    print(word_token)
    n_gram_wordlist=[]
    for idx in range(len(word_token)-n_gram+1):
        n_gram_wordlist.append(word_token[idx:idx+n_gram])
    return n_gram_wordlist

