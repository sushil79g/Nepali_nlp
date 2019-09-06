import gensim
from gensim.models.keyedvectors import KeyedVectors

#soon S3 bucket link will be provided.This is just for test
def load_vector():
    """Download and load embedding. #This is private embedding I will update link later
    
    Returns:
        [keyedVectors] -- [Custom Nepali word Embedding]
    """
    from google.colab import drive
    drive.mount('/content/drive')
    base_folder = 'drive/My Drive/dataset/NepaliEmbed/'
    word_vector = KeyedVectors.load(base_folder + 'word_vector.sg')
    
    return word_vector

