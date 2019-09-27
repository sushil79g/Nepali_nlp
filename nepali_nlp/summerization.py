from Embedding import Embeddings
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
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

    def sentence_vectorizer(sentence,size):
        dic = {}
        for i in range(len(sentence)):
            sum_vec = np.zeros(size)
            try:
                sentence_word = sentence[i].split()
            except:
                pass
            sentence = [word for word in sentence_word if word in self.vocab]
            if sentence:
                for word in sentence:
                    word_vec_ = self.word_vec[word]
                    sum_vec = np.add(sum_vec, word_vec_)
                dic[i] = sum_vec/len(sentence)
        return dic

    def sentence_selection(centroid, sentences_dict, summary_length):
        from scipy.spatial.distance import cosine
        sentence_retriever = []
        record = []

        for sentence_id in sentences_dict:
            vector = sentences_dict[sentence_id]
            similarity = (1- cosine(centroid, vector))
            record.append((sentence_id, vector, similarity))

        rank = list(reversed(sorted(record, key= lambda tup: tup[2])))
        sentence_ids = []
        summary_char_num = 0 
        stop = False
        i = 0 
        text_length = sum( [len(x) for x in sentence_retriever])

        if summary_length <1:
            limit = int(text_length * float(summary_length))

            while not stop and i < len(rank):
                sentence_id = rank[i][0]
                new_vector = sentences_dict[sentence_id]
                sent_char_num = len(sentence_retriever[sentence_id])
                redundancy = [sentences_dict[k] for k in sentence_ids
                             if (1- cosine(new_vector, sentences_dict[k]) > 0.95)]
                
                if not redundancy:
                    summary_char_num += sent_char_num
                    sentence_ids.append(sentence_id)
                
                i = i + 1

                if summary_char_num > limit:
                    stop = True
                
        else:
            sentences_number = int(summary_length)
            sentence_ids = rank[:sentences_number]
            sentence_ids = map(lambda t:t[0], sentence_ids)
        
        sentence_ids = sorted(sentence_ids)

        return sentence_ids

