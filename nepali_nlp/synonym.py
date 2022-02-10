import sys
sys.path.append('..')

from .Embedding import Embeddings

class Synonym:
    
    def __init__(self):
        pass

    def raw_synonym(self,word, word_vec):
        """show the similar words according to embedding
        
        Arguments:
            word{string} -- word you want to find synonym
        
        Returns:
            [tuple]: synonym word with similarity score
        """
        
        synonyms = word_vec.most_similar(word)

        return synonyms


    def filter_synonym(self,word, word_vec):
        """Funtion to filter the similarity words from embedding
        
        Arguments:
            word {string} -- [word to find similar words]
        
        Returns:
            [list] -- [similar words]
        """
        syno = []
        synonyms = word_vec.most_similar(word)
        for words in synonyms:
            if word not in words[0]:
                syno.append(words)
        
        return syno

    def __str__(self):
        return "return filtered and un-filtered synonyms for Nepali word."
