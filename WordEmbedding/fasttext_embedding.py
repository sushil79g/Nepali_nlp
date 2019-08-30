import wget
import gzip
from gensim.models.keyedvectors import KeyedVectors
def load_fasttext(link="https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ne.300.vec.gz"):
    fil_ = wget.download(link)
    print('embedding_downloaded')
    abc = gzip.open(fil_, 'rb')
    file_content = abc.read()
    abc.close()
    model = KeyedVectors.load_word2vec_format(file_content, binary=False)
    model.save_word2vec_format('wiki.np.txt',binary=False)
    return model
