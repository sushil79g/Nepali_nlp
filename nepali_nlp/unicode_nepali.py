import collections
from collections import OrderedDict
from pprint import pprint

from nepali_nlp.tokenize import convert_word

nepali =  {
    'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ii': 'ई', 'u': 'उ', 'uu': 'ऊ', 'e': 'ए', 'ai': 'ऐ', 'o': 'ओ', 'au': 'औ', 'k': 'क्',
    'ka': 'क', 'kh': 'ख्', 'kha': 'ख', 'g': 'ग्', 'ga': 'ग', 'gh': 'घ्', 'gha': 'घ', 'ch': 'च्', 'cha': 'च', 'chh': 'छ्', 'chha': 'छ',
    'j': 'ज्', 'ja': 'ज', 'jh': 'झ्', 'jha': 'झ', 't': 'त्', 'ta': 'त', 'tha': 'थ', 'th': 'थ्', 'T': 'ट्', 'Ta': 'ट', 'Th': 'ठ्', 'Tha': 'ठ',
    'd': 'द्', 'da': 'द', 'D': 'ड्', 'Da': 'ड', 'Dh': 'ढ्', 'Dha': 'ढ', 'dh': 'ध्', 'dha': 'ध', 'n': 'न्', 'na': 'न', 'Ng': 'ङ्', 'Nga': 'ङ',
    'N': 'ण्', 'Na': 'ण', 'Yn': 'ञ्', 'Y': 'य्', 'Ya': 'य', 'Yna': 'ञ', 'p': 'प्', 'pa': 'प', 'ph': 'फ्', 'pha': 'फ', 'b': 'ब्', 'ba': 'ब', 
    'bh': 'भ्', 'bha': 'भ', 'm': 'म्', 'ma': 'म', 'y': 'य्', 'ya': 'य', 'r': 'र्', 'ra': 'र', 'rr': 'र्‍', 'l': 'ल्', 'la': 'ल', 'v': 'व्', 
    'va': 'व', 'sh': 'श्', 'sha': 'श', 's': 'स्', 'sa': 'स', 'shh': 'ष्', 'shha': 'ष', 'h': 'ह्', 'ha': 'ह', 'c': 'क्', 'ca': 'क', 'f': 'फ्', 
    'fa': 'फ', 'q': 'क्', 'qa': 'क', 'w': 'व्', 'wa': 'व', 'x': 'ज्', 'xa': 'ज', 'z': 'ज्', 'za': 'ज', 'O': 'ॐ'
}
halanta = {
    'k':'ka','kh':'kha','g':'ga','gh':'gha','ch':'cha','chh':'chha','j':'ja','jh':'jha','t':'ta','th':'tha','T':'Ta','Th':'Tha','d':'da',
    'D':'Da','Dh':'Dha','dh':'dha','n':'na','Ng':'Nga','N':'Na','Y':'Ya','p':'pa','ph':'pha','b':'ba','bh':'bha','m':'ma','y':'ya','r':'ra',
    'l':'la','v':'va','sh':'sha','s':'sa','shh':'shha','h':'ha','c':'ca','f':'fa','q':'qa','w':'wa','x':'xa','z':'za'
}
sabda_banot = {
    'aa': 'ा', 'i': 'ि', 'ii': 'ी', 'u': 'ु', 'uu': 'ू', 'e': 'े', 'ai': 'ै', 'o': 'ो', 'au': 'ौ'
}
exception= {'au': 'औ', 'garchu':'गर्छु','aauda': 'आउँदा', 'acharya': 'आचार्य', 'airport': 'एअरपोर्ट', 'amrit': 'अमृत', 
            'char': 'चार', 'chhetri': '', 'paanch': 'पाँच', 'facebook': 'फेसबुक', 'fortystones': 'फोर्टिस्टोन्स', 'kathmandu': 'काठमाडौं', 
            'kripaya': 'कृपया', 'krishi': 'कृषि', 'krishna': 'कृष्ण', 'krishnaa': 'कृष्णा', 'patan': 'पाटन', 'tapai': 'तपाईं', 'gyan': 'ज्ञान', 
            'rajbhandari': 'राजभण्डारी', 'roushan': 'रौशन','shah': 'शाह', 'shrestha': 'श्रेष्ठ', 'unicode': 'युनिकोड', 'united': 'युनाईटेड','gardai':'गर्दै','gardaichhu':'गर्दैछु'}

def unicode_word(text):
   if text in exception.keys():
      return exception[text]

   combine_latter = {**nepali, **sabda_banot}
   ship = collections.OrderedDict(combine_latter)
   latter_dict = OrderedDict(sorted(combine_latter.items(), key=lambda x: len(x[0]),reverse=True))
   split = []
   keys = list(latter_dict.keys())
   c = 0
   while text != "":
      key_collection = keys.copy()
      for key in key_collection:
         if key == text[:len(key)]:
               split.append(key)
               text = text[len(key):]
               c = 1
               break
      if c== 1:
         c = 0
         continue
      if not text:
         break
      split.append(text[0])
      text = text[1:]
   actual_text = ''
   for latter in split:
      if latter in nepali:
         actual_text = actual_text + str(nepali[latter])
      elif latter in sabda_banot:
         actual_text = actual_text + str(sabda_banot[latter])

   for index in range(1, len(split)-1):
      if split[index] in sabda_banot:
         if split[index-1] in halanta:
               split[index-1] = halanta[split[index-1]]
               continue
         else:
               if  split[index-2] in halanta:
                  split[index-2] = halanta[split[index-2]]
               continue

   if split[-1] in halanta:
      split[-1] = halanta[split[-1]]
   word = ''
   for item in split:
      word = word + str(latter_dict[item])
   return word

def unicode_sentence(sentence):
   
   texts =convert_word(sentence)
   convert_nepali = ''
   for text in texts:
      if text in exception.keys():
         convert_nepali = convert_nepali + ' ' + exception[text]
         continue

      combine_latter = {**nepali, **sabda_banot}
      ship = collections.OrderedDict(combine_latter)
      latter_dict = OrderedDict(sorted(combine_latter.items(), key=lambda x: len(x[0]),reverse=True))
      split = []
      keys = list(latter_dict.keys())
      c = 0
      while text != "":
         key_collection = keys.copy()
         for key in key_collection:
            if key == text[:len(key)]:
                  split.append(key)
                  text = text[len(key):]
                  c = 1
                  break
         if c== 1:
            c = 0
            continue
         if not text:
            break
         split.append(text[0])
         text = text[1:]
      actual_text = ''
      for latter in split:
         if latter in nepali:
            actual_text = actual_text + str(nepali[latter])
         elif latter in sabda_banot:
            actual_text = actual_text + str(sabda_banot[latter])

      for index in range(1, len(split)-1):
         if split[index] in sabda_banot:
            if split[index-1] in halanta:
                  split[index-1] = halanta[split[index-1]]
                  continue
            else:
                  if  split[index-2] in halanta:
                     split[index-2] = halanta[split[index-2]]
                  continue

      if split[-1] in halanta:
         split[-1] = halanta[split[-1]]
      word = ''
      for item in split:
         word = word + str(latter_dict[item])
      convert_nepali = convert_nepali + ' ' + word
   
   return convert_nepali