import string

def sentence_tokenize(text):
    """This function tokenize the sentences
    
    Arguments:
        text {string} -- Sentences you want to tokenize
    
    Returns:
        sentence {list} -- tokenized sentence in list
    """
    sentences = text.split(u"।")
    sentences = [sentence.translate(str.maketrans('', '', string.punctuation)) for sentence in sentences]
    return sentences

def word_tokenize(sentece):
    """This function tokenize with respect to word
    
    Arguments:
        sentece {string} -- sentence you want to tokenize 
    
    Returns:
        list -- tokenized words
    """
    punctuations = ['।',',',';','?','!','—','-']
    for punct in punctuations:
        text = ' '.join(text.split(punct))
    return text.split()
