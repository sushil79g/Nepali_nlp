nepali =  {
    'a': 'अ', 'aa': 'आ', 'i': 'इ', 'ii': 'ई', 'u': 'उ', 'uu': 'ऊ', 'e': 'ए', 'ai': 'ऐ', 'o': 'ओ', 'au': 'औ', 'k': 'क्', 'ka': 'क', 'kh': 'ख्', 'kha': 'ख', 'g': 'ग्', 'ga': 'ग', 'gh': 'घ्', 'gha': 'घ', 'ch': 'च्', 'cha': 'च', 'chh': 'छ्', 'chha': 'छ', 'j': 'ज्', 'ja': 'ज', 'jh': 'झ्', 'jha': 'झ', 't': 'त्', 'ta': 'त', 'tha': 'थ', 'th': 'थ्', 'T': 'ट्', 'Ta': 'ट', 'Th': 'ठ्', 'Tha': 'ठ', 'd': 'द्', 'da': 'द', 'D': 'ड्', 'Da': 'ड', 'Dh': 'ढ्', 'Dha': 'ढ', 'dh': 'ध्', 'dha': 'ध', 'n': 'न्', 'na': 'न', 'Ng': 'ङ्', 'Nga': 'ङ', 'N': 'ण्', 'Na': 'ण', 'Yn': 'ञ्', 'Y': 'य्', 'Ya': 'य', 'Yna': 'ञ', 'p': 'प्', 'pa': 'प', 'ph': 'फ्', 'pha': 'फ', 'b': 'ब्', 'ba': 'ब', 'bh': 'भ्', 'bha': 'भ', 'm': 'म्', 'ma': 'म', 'y': 'य्', 'ya': 'य', 'r': 'र्', 'ra': 'र', 'rr': 'र्‍', 'l': 'ल्', 'la': 'ल', 'v': 'व्', 'va': 'व', 'sh': 'श्', 'sha': 'श', 's': 'स्', 'sa': 'स', 'shh': 'ष्', 'shha': 'ष', 'h': 'ह्', 'ha': 'ह', 'c': 'क्', 'ca': 'क', 'f': 'फ्', 'fa': 'फ', 'q': 'क्', 'qa': 'क', 'w': 'व्', 'wa': 'व', 'x': 'ज्', 'xa': 'ज', 'z': 'ज्', 'za': 'ज', 'O': 'ॐ'
}
sabda_banot = {
    'aa': 'ा', 'i': 'ि', 'ii': 'ी', 'u': 'ु', 'uu': 'ू', 'e': 'े', 'ai': 'ै', 'o': 'ो', 'au': 'ौ'
}
vowel ={
    'a': '', 'i': '', 'u': '', 'e': '', 'o': ''
}
consonant = {
    'b': '', 'c': '', 'd': '', 'D': '', 'f': '', 'g': '', 'h': '', 'j': '', 'k': '', 'l': '', 'm': '', 'n': '', 'N': '', 'p': '', 'q': '', 'r': '', 's': '', 't': '', 'T': '', 'Y': '', 'O': '', 'v': '', 'w': '', 'y': '', 'x': '', 'z': ''
}
numerals =  {
    0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''
}
special_character = {
    '`':'','~':'','!':'','@':'','#':'','$':'','%':'','&':'',
    '(': '', ')':'', '-':'', '_':'', '=':'', '+':'', '{': '', '}': '', '[': '', ']': '', '\\': '', '|': '', ';': '', ':': '', '"': '', '\'': '', '<': '', '>': '', ',': '', '.': '', '?': '', '/': '', 'A': '', 'B': '', 'C': '', 'E': '', 'F': '', 'G': '', 'H': '', 'I': '', 'J': '', 'K': '', 'L': '', 'M': '', 'P': '', 'Q': '', 'R': '', 'S': '', 'U': '', 'V': '', 'W': '', 'X': '', 'Z': ''
}
mystruct = {
    "a":("aa", "ai", "au", "a"), "b":("bh", "b", "ba", "bha"), "c":("chh", "ch", "cha", "c", "ca", "chha"), "d":("d", "da", "dh", "dha"), "D":("D", "Da", "Dh", "Dha"), "e":("e"), "f": ("f", "fa"), "g":("gh", "gha", "g", "ga"), "h":("h", "ha"), "i":("ii", "i"), "j":("jh", "jha", "j", "ja"), "k":("kh", "kha", "k", "ka"), "l":("l", "la"), "m":("m", "ma"), "n":("n", "na"), "N":("N", "Na", "Ng", "Nga"), "o":("o"), "O":("O"), "p":("ph", "pha", "p", "pa"), "q":("q", "qa"), "r":("r", "ra", "rr"), "s":("shh", "shha", "sh", "sha", "s", "sa"), "t":("th", "tha", "t", "ta"), "T":("T", "Ta", "Th", "Tha"), "u":("uu", "u"), "v":("v", "va"),"w":("w", "wa"), "x":("x", "xa"), "y":("y", "ya"), "Y":("Y", "Ya", "Yn", "Yna"), "z":("zh", "z", "za")
}
flg = "";result="";code="";code_support="";flag_for_shabda_banot=False
taggleon=False;word=""

def resetflags():
  global taggleon,result,code,code_support,flag_for_shabda_banot,word
  flag_for_shabda_banot=False

def initialize(val):
  global flg
  flg = mystruct[val[len(val) - 1]]

def changeinDisplay(val):
  if len(val)<2:
    return None
  global result
  result = result[:-2]

def changeinDisplay2(val):
  global code,vowel, consonant, result,code_support
  if code[len(code)-1] in vowel and code[len(code)-2] in consonant:
    result = result[:-1]
  if(((code_support[len(code_support)-1]=="i") and (code[len(code)-2]=="i")) or ((code_support[len(code_support)-1]=="u") and (code[len(code)-2]=="u"))):
    result = result[:(len(result)-1)]
  return None

def display(result_temp):
  global result
  result = result + result_temp
  print(result)

def spacebarPressed(){
  global code_support="",code="",flag_for_shabda_banot=False
  display('\u0020')
}

def enterkeyPressed():
  global code_support="",code="",flag_for_shabda_banot=False
  display("\n")

def Unicode():
  global val,numerals,special_character,code,code_support,vowel,consonant,flag_for_shabda_banot
  last_latter = val[len(val)-1]
  if last_latter in numerals or last_latter in special_character:
    display(last_latter)
    flag = "e"
    return None 
  
  found = False
  code = code + last_latter
  if code_support[len(code_support) - 1] in vowel and last_latter in consonant:
    code_support = ""
  if flag_for_shabda_banot==True:
    



