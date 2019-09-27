from Embedding import Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
class Summerize:
    def __init__(self, *args, **kwargs):
        pass

    def generate_centroid_tfidf(self, sentence):
        tf = TfidfVectorizer()
        