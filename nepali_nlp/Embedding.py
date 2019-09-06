import gensim
from gensim.models.keyedvectors import KeyedVectors
from nepali_nlp.Download_embedding import download_file_from_google_drive

def load_vector():
    """Download and load embedding. #This is private embedding I will update link later
    
    Returns:
        [keyedVectors] -- [Custom Nepali word Embedding]
    """
    download_file_from_google_drive('1ik38vahOmzhiU2DBi78VOqDt7YFPsk5w','word_vector.sg')
    word_vector = KeyedVectors.load('word_vector.sg')
    
    return word_vector

def load_large_vector():
    """Returns a large Nepali word embedding. Creator: https://github.com/rabindralamsal/Word2Vec-Embeddings-for-Nepali-Language
       
    Returns:
        [keyedVectors] -- [Custom Nepali word Embedding]
    """
    download_file_from_google_drive('1KnAZ2Eeqwz3S9VrAuzTLWysAaRB6Ch7e','nepali_embeddings_word2vec.txt')
    word_vector = KeyedVectors.load('nepali_embeddings_word2vec.txt')

    return word_vector

