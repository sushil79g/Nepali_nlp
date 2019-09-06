
from tokenize import word_tokenize

def remove_stopwords(text):
    """This function remove stopwords from text
    
    Arguments:
        sentence {string} -- sentence you want to remove stopwords
        
    Returns:
        list -- token words
    """
    f = open("local_dataset/stopword.txt",'r')
    stopwords = f.read()
    stopwords = stopwords.split("\n")[5:]
    token = word_tokenize(text)
    word_without_stopword=[]
    for word in token:
        if word not in stopwords:
            word_without_stopword.append(word)
        
    return word_without_stopword
