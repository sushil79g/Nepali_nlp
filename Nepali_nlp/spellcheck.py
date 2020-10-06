# coding: utf-8
import os
import sys 
sys.path.append('..')
from spello.model import SpellCorrectionModel

from difflib import get_close_matches

class Corrector:
    """This function correct the Nepali word based on distance of character.
    
    """
    def __init__(self):
        self.this_dir, self.this_file = os.path.split(__file__)
        self.sp = SpellCorrectionModel(language='hi').load(os.path.join(self.this_dir, "local_dataset", "spell_model.pkl"))

    def __load_words(self,location):
        """This function load all the Nepali words in given location.
        
        Arguments:
            location {string} -- [Location where vocabulary is located please be sure to indicate name and extension also.]
        
        Returns:
            [list] -- [List of all Nepali word]
        """
        file = open(os.path.join(self.this_dir,"local_dataset", location), 'r')
        text = file.read()
        text = text.split()
        file.close()
        return text

    def corrector(self,word,location ='words.txt',number=2, threshold = 0.3):
        """This functon returns 'n' number of correct words.
        
        Arguments:
            word {string} -- [Word you want to check for spelling.]
        
        Keyword Arguments:
            location {str} -- [Location of Vocabulary file with name and extension.] (default: {'../local_dataset/words.txt'})
            number {int} -- [Number of close correct words.] (default: {2})
            threshold {float} -- [Threshold distance between words enter and predicted word'.] (default: {0.3})
        
        Returns:
            [list] -- ['n' correct word predictions.]
        """
        word_list = self.__load_words(location)
        matches = get_close_matches(word, word_list, n=2, cutoff=0.3)

        return matches

    def spell_correct(self, text):
        """
        Returns the spell corrected string based on context, phoneme

        Arguments:
            text {str} -- Text in Nepali

        Returns:
            Dict -- dictionary with correct word, input text and correction text.
        """
        return self.sp.spell_correct(text)

