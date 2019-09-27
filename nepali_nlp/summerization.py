from Embedding import Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
class Summerize:
    def __init__(self, *args, **kwargs):
        # this should not be the stander way of doing.
        print('loading embedding')
        self.word_vec = Embedding().load_vector()
        self.vocab = word_vec.vocab
        print('everything loaded')

    def generate_centroid_tfidf(self, sentence):
        tf = TfidfVectorizer()
        tfidf = tf.fit_transfor(sentenct).toarray().sum(0)
        tfidf = np.divide(tfidf, tfidf.max())
        words = tf.get_feature_names()
        similar_term = []

        for i in range(len(tfidf)):
            if words[i] in self.vocab:
                if tfidf[i] >=0.2:
                    similar_term.append(words[i])
        
        res = [self.word_vec[term] for term in similar_term]
        return sum(res)/len(res)
