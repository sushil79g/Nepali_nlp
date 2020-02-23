import wget
import gzip
from gensim.models.keyedvectors import KeyedVectors


class Fasttext:
    """Load fasttext Nepali embedding"""

    def __init__(self):
        pass

    def load(self, link="https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ne.300.vec.gz"):
        """This function load fasttext embeddings for nepali
        
        Keyword Arguments:
            link {str} -- link of binary embedding for Nepali (default: {"https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ne.300.vec.gz"})
        
        Returns:
            keyebvector model -- Embedding model
        """
        fil_ = wget.download(link)
        print('embedding_downloaded')
        abc = gzip.open(fil_, 'rb')
        file_content = abc.read()
        abc.close()
        model = KeyedVectors.load_word2vec_format(file_content, binary=False)
        model.save_word2vec_format('wiki.np.txt', binary=False)
        return model

    def __str__(self):
        return "Fasttext embedding from https://fasttext.cc/docs/en/crawl-vectors.html"
