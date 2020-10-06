import sys
sys.path.append('..')

from .Embedding import Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import string
class Summerize:
    def __init__(self, *args, **kwargs):
        # This should not be the standard way of doing. Standard way will be done in next iteration.
        # print('Loading Embedding')
        # self.word_vec = Embeddings().load_vector()
        # self.vocab = self.word_vec.vocab
        # print('Embedding is now loaded')
        pass

    def preprocess(self,text):
        """This function remove punctuation and split text in sentences.
        
        Arguments:
            text {String} -- [Nepali text paragraph]
        
        Returns:
            [list] -- [list of sentences]
        """
        sentences = text.split(u"।")
        sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
        return sentences
    
    def generate_centroif_tfidf(self,word_vec,sentence):
        """This function generates tfidf value for each sentences
        
        Arguments:
            sentence {[list]} -- [list of sentence in paragraph]
        
        Returns:
            [array] -- [mathmatical representation for centroid]
        """
        tf = TfidfVectorizer()
        tfidf = tf.fit_transform(sentence).toarray().sum(0)
        tfidf = np.divide(tfidf, tfidf.max())
        words = tf.get_feature_names()
        similar_term = []
        for i in range(len(tfidf)):
            if words[i] in word_vec.vocab:
                if tfidf[i] >= 0.2:
                    similar_term.append(words[i])
        res = [word_vec[term] for term in similar_term]
        return sum(res)/len(res)

    def sentence_vectorizer(self,word_vec,sentence,size):
        """This function vectorize the passed sentence for the given size
        
        Arguments:
            sentence {list} -- [list of sentence in Nepali text paragraph]
            size {int/tuple} -- [size of word embedding vector]
        
        Returns:
            [dictionary] -- [vectorize value for every sentence]
        """
        dic = {}
        for i in range(len(sentence)):
            sum_vec = np.zeros(size)
            try:
                sentence_word = sentence[i].split()
            except:
                pass
            sentence = [word for word in sentence_word if word in word_vec.vocab]
            if sentence:
                for word in sentence:
                    word_vec_ = word_vec[word]
                    sum_vec = np.add(sum_vec, word_vec_)
                    
                dic[i] = sum_vec/len(sentence)
        return dic

    def sentence_selection(self,centroid, sentences_dict, summary_length):
        """This function helps to select the most important sentece.
        
        Arguments:
            centroid {array} -- [tf/idf values of centroid]
            sentences_dict {array} -- [Vectorized value of every sentence]
            summary_length {int/float} -- [Number of summerized sentence desired.]
        
        Returns:
            [list] -- [list of sentence id selected.]
        """
        from scipy.spatial.distance import cosine
        sentence_retriever = []
        record = []
        for sentence_id in sentences_dict:
            vector = sentences_dict[sentence_id]
            similarity = (1 - cosine(centroid, vector))
            record.append((sentence_id, vector, similarity))

        rank = list(reversed(sorted(record, key=lambda tup: tup[2])))
        sentence_ids = []
        summary_char_num = 0
        stop = False
        i = 0
        text_length = sum([len(x) for x in sentence_retriever])

        if summary_length < 1:
            limit = int(text_length * float(summary_length))

            while not stop and i < len(rank):
                sentence_id = rank[i][0]
                new_vector = sentences_dict[sentence_id]
                sent_char_num = len(sentence_retriever[sentence_id])
                redundancy = [sentences_dict[k] for k in sentence_ids
                                if (1 - cosine(new_vector, sentences_dict[k]) > 0.95)]

                if not redundancy:
                    summary_char_num += sent_char_num
                    sentence_ids.append(sentence_id)
                i += 1

                if summary_char_num > limit:
                    stop = True
        else: 
            sentences_number = int(summary_length)
            sentence_ids = rank[:sentences_number]
            sentence_ids = map(lambda t: t[0], sentence_ids)

        sentence_ids = sorted(sentence_ids)
        
        return sentence_ids

    def combine_sentence(self,centroid_tfidf,sent,sent_dict,length):
        """This function helps to combine summerized sentence.
        
        Arguments:
            centroid_tfidf {array} -- [vectorized value of centroid.]
            sent {list} -- [list of sentence in text]
            sent_dict {dictionary} -- [Vectorized value of every sentence.]
            length {int/float} -- [Number of desired sentence.]
        
        Returns:
            [string] -- [Paragraph of combine summerize sentence.]
        """
        ids = self.sentence_selection(centroid_tfidf,sent_dict,length)
        whole_summary = []
        for inde in ids:
            whole_summary.append(sent[inde])
        return '।'.join(whole_summary)


    def show_summary(self, word_vec,sample_text,length_sentence_predict):
        sent = self.preprocess(sample_text)
        centroid_tfidf = self.generate_centroif_tfidf(word_vec,sent)
        size = word_vec.vector_size
        sent_dict = self.sentence_vectorizer(word_vec,sent,size)
        return self.combine_sentence(centroid_tfidf,sent,sent_dict,length_sentence_predict)