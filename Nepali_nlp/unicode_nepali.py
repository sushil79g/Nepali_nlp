import sys 
sys.path.append('..')

import collections
from collections import OrderedDict
from pprint import pprint

from .local_dataset.unicode import nepali, halanta, sabda_banot, exception

class Unicode:
   """This class converts Roman written Nepali word to actual Nepali word."""
   def __init__(self, *args, **kwargs):
      pass
   
   def unicode_word(self,text):
      """Function converts Unicode words(i.e Roman word like 'nepal') to actual Nepali word.
      
      Arguments:
          text {string} -- Unicode 'word' to convert
      
      Returns:
          [string] -- [Converted Nepali word.]
      """
      text = text.replace('aa','aaa') #To solve the common pattern Roman writing
      if text in exception.keys():
         return exception[text]

      combine_latter = {**nepali, **sabda_banot}
      latter_dict = OrderedDict(sorted(combine_latter.items(), key=lambda x: len(x[0]),reverse=True)) #We are going through reverse lenth of user input roman i.e first check 'kha' than check 'ka'
      split = [] #to automatically store the predicted possible words in roman from user input text.
      keys = list(latter_dict.keys())
      c = 0 #counter to get out of loop.
      
      while text != "":#until every word are not converted
         key_collection = keys.copy()
         #To split the text according to the mapping word list in key_collection.
         for key in key_collection:
            if key == text[:len(key)]:
                  split.append(key)
                  text = text[len(key):]
                  c = 1
                  break
         
         if c== 1:# to continue out of loop. It can be done by other ways too.
            c = 0
            continue
         
         if not text: #if text is empty, breaking the loop.
            break
         
         split.append(text[0])
         text = text[1:] #if nothing is found in text which can be mapped, we leave the initial latter.. we will be taking care about that soon.
      
      actual_text = ''
      #converting all the possible single syallabyal of roman to Nepali.
      for latter in split:
         if latter in nepali:
            actual_text = actual_text + str(nepali[latter])
         elif latter in sabda_banot:
            actual_text = actual_text + str(sabda_banot[latter])

      #Taking care of Khutta kateko character of Nepali.
      for index in range(len(split)):
         if split[index] in sabda_banot:
            if split[index-1] in halanta:
                  split[index-1] = halanta[split[index-1]]
                  continue
            else:
                  if  split[index-2] in halanta:
                     split[index-2] = halanta[split[index-2]]
                  continue

      #if khutta kateko appears in last character: Going to make a single character i.e r=>ra.
      if split[-1] in halanta:
         split[-1] = halanta[split[-1]]
      
      #Summing up everything.
      word = ''
      for item in split:
         try:
            word = word + str(latter_dict[item])
         except:
            word = word + ' '
      
      return word

