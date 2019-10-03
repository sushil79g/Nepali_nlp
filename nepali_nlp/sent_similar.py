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

# model = Embeddings().load_vector()
# sim = compute_sentence_similarity(sent_1, sent_2, model)
