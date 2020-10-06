import os
import sys
sys.path.append('..')

import gensim
from gensim.models.keyedvectors import KeyedVectors
from .Download_embedding import Download

class Embeddings:
    """This class helps to load embedding in keyedvector format."""

    def __init__(self):
        pass

    def load_large_vector(self):
        """Download and load embedding. #This is private embedding I will update link later

        Returns:
            [keyedVectors] -- [Custom Nepali word Embedding]
        """
        download = Download()
        download.download_file_from_google_drive('1ik38vahOmzhiU2DBi78VOqDt7YFPsk5w', 'word_vector.sg')
        word_vector = KeyedVectors.load_word2vec_format('word_vector.sg', binary=False)
        os.remove("word_vector.sg")

        return word_vector

    def load_vector(self):
        """Returns a large Nepali word embedding. Creator: https://github.com/rabindralamsal/Word2Vec-Embeddings-for-Nepali-Language
        
        Returns:
            [keyedVectors] -- [Custom Nepali word Embedding]
        """
        download = Download()
        download.download_file_from_google_drive('1KnAZ2Eeqwz3S9VrAuzTLWysAaRB6Ch7e', 'nepali_embeddings_word2vec.txt')
        word_vector = KeyedVectors.load('nepali_embeddings_word2vec.txt')
        os.remove("nepali_embeddings_word2vec.txt")
        
        return word_vector

    def __str__(self):
        return "Required to load different emebeddings"
