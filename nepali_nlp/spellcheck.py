# coding: utf-8
import sys 
sys.path.append('..')

from difflib import get_close_matches

def load_words(location ='../local_dataset/words.txt'):
    file = open(location, 'r', encoding="utf8")
    text = file.read()
    txt = text.split()
    file.close()
    return text

def corrector(word,number=2, threshold = 0.3):
    word_list = load_words()
    matches = get_close_matches(word, word_list, n=number, cutoff=threshold)

    return matches

print(len(corrector('वह्किल')))
