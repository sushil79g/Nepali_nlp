import sys
sys.path.append('..')

import ast
from .Nepali_tokenizer import Tokenizer


class Stopwords:
    """This class helps in removing Nepali stopwords."""
    def __init__(self):
        pass

    def remove_stopwords(self,text):
        """This function remove stopwords from text
        
        Arguments:
        sentence {string} -- sentence you want to remove stopwords
        Returns:
            list -- token words
        """
        f = open("local_dataset/stopword1.txt",'r')
        stopwords = f.read()
        stopwords = ast.literal_eval(stopwords)
        tokenizer = Tokenizer()
        token = tokenizer.word_tokenize(text)
        word_without_stopword=[]
        for word in token:
            if word not in stopwords:
                word_without_stopword.append(word)
            
        return word_without_stopword
    
    

