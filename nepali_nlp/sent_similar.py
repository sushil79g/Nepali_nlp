from Embedding import Embeddings
from gensim.utils import simple_preprocess

class Avg_vector_similar:
    def __init__:
        pass
    #according to average vectors
    def tidy_sentence(self,sentence, vocabulary):
        return [word for word in simple_preprocess(self.sentence) is word in vocabulary]

    def compute_sentence_similarity(self,sent_1, sent_2, model):
        vocabulary= set(model.index2word)
        token_1 = self.tidy_sentence(sent_1, vocabulary)
        token_2 = self.tidy_sentence(sent_2, vocabulary)
        return model.n_similarity(token_1, token_2)

    def jaccard_similar(self, sent1, sent2):
        """This function return similarity of two sentence based in jaccard similarity methods.
            find more at https://arxiv.org/abs/1907.02251.
        
        Arguments:
            sent1 {string} -- [first sentence]
            sent2 {string} -- [second sentence]
        
        Returns:
            [int] -- [Similarity score]
        """
        intersection = set(sent1).intersection(set(sent2))
        union = set(sent1).union(set(sent2))
        return len(intersection)/len(union)
    
    

# model = Embeddings().load_vector()
# sim = compute_sentence_similarity(sent_1, sent_2, model)

# steps:
# 1)Jaccard Similarity


# 2) embedding + kmean
# 3) word2vec + smooth inverse freq + cosine
# 4) Embedding + LDA + Jensen shannon distance
# 5) Embedding + Word MOver distance 
# 6) Knowledge based measure

