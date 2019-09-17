# coding: utf-8
import sys 
sys.path.append('..')

from difflib import get_close_matches

def load_words(location ='../local_dataset/words.txt'):
    file = open(location, 'r')
    text = file.read()
    text = text.split()
    file.close()
    return text

def corrector(word,number=2, threshold = 0.3):
    word_list = load_words()
    matches = get_close_matches(word, word_list, n=2, cutoff=0.3)

    return matches

