from WordEmbedding.Embedding import load_vector
def raw_synonym(word):
    """show the similar words according to embedding
    
    Arguments:
        word{string} -- word you want to find synonym
    
    Returns:
        [tuple]: synonym word with similarity score
    """
    word_vec = load_vector()
    synonyms = word_vec.most_similar(word)

    return synonyms


def filter_synonym(word):
    """Funtion to filter the similarity words from embedding
    
    Arguments:
        word {string} -- [word to find similar words]
    
    Returns:
        [list] -- [similar words]
    """
    word_vec = load_vector()
    abc = word_vec.most_similar(word)
    syno = []
    for words in abc:
        if word not in words[0]:
            syno.append(words)
    
    return syno
