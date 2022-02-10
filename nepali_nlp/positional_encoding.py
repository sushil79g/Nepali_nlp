import sys
sys.path.append('..')

import numpy as np
from .Nepali_tokenizer import Tokenizer

class PositionalEncoding:
    """This class helps to encoding the  tokenized text based on the postion of the word."""

    def __init__(self, vector_dim):
        self.vector_dim = vector_dim

    def encode(self,token):
        """This function generate  the embedding of text based on postion
        
        Arguments:
            token {list} -- List of tokens of sentences
        
        Returns:
            2Darray {numpy.ndarray} -- 2D embedding for the tokens based on postions


        -----------------------Test Case-------------------------------------- 
        test_data = "सहकारी भन्नासाथ नगदको कारोबार अर्थात वचत संकलन र ऋण लगानी गर्ने संस्था भन्ने आम धारणा छ"
        token = Tokenizer()
        token_text = token.word_tokenize(test_data)
        posencode = PositionalEncoding(10)
        print(posencode.encode(token_text))
     
        """
        
        encoding_vector = np.zeros((len(token),self.vector_dim),dtype=float)
        for row in range(len(token)):
            i=1
            for column in range(0,int(self.vector_dim),2):
                w = 1/(pow(1000,2*i/self.vector_dim))
                encoding_vector[row][column] = np.sin(w*row)
                encoding_vector[row][column+1] = np.cos(w*row)
                # print(row,column,i,np.sin(w*(row+1)))
                # print(row,column+1,i,np.cos(w*(row+1)))
                i+=1
        return encoding_vector



