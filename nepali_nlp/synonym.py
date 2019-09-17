from nepali_nlp.Embedding import Embeddings

class Synonym:
    
    def load_embedding(self, load_large=False):
        """This function load the embeddings. 
        
        Keyword Arguments:
            load_large {bool} -- IF True it will load the large Nepali embedding else it will load comparitibly small Nepali embedding.(default: {False})
        
        Returns:
            keyedVector -- Returns the embedding in keyedvector format.
        """
        embedding = Embeddings()
        if load_large:
            word_vec = embedding.load_large_vector()
        else:
            word_vec = embedding.load_vector()
        
        return word_vec

    def raw_synonym(self,word, load_large=False):
        """show the similar words according to embedding
        
        Arguments:
            word{string} -- word you want to find synonym
        
        Returns:
            [tuple]: synonym word with similarity score
        """
        
        word_vec = self.load_embedding(load_large)
        synonyms = word_vec.most_similar(word)

        return synonyms


    def filter_synonym(self,word,load_large=False):
        """Funtion to filter the similarity words from embedding
        
        Arguments:
            word {string} -- [word to find similar words]
        
        Returns:
            [list] -- [similar words]
        """
        word_vec = self.load_embedding(load_large)
        syno = []
        synonyms = word_vec.most_similar(word)
        for words in synonyms:
            if word not in words[0]:
                syno.append(words)
        
        return syno

    def __str__(self):
        return "return filtered and un-filtered synonyms for Nepali word."
