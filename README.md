# Nepali_nlp: A NLP library for Nepali Language
> This projects aims to build a library for all the NLP processes for Nepali Language.

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Nepali_nlp)
![PyPI - Downloads](https://img.shields.io/pypi/dm/Nepali_nlp)
[![GitHub license](https://img.shields.io/github/license/sushil79g/Nepali_nlp)](https://github.com/sushil79g/Nepali_nlp/blob/master/LICENSE)

## Getting the module

```bash
sudo apt install libicu-dev

pip install gensim==3.7.3 requests==2.22.0 wget==3.2 beautifulsoup4 news-please pytesseract spello==1.2.0 snowballstemmer scikit-learn==0.23.2 opencv-python pyicu

pip install git+https://github.com/sushil79g/Nepali_nlp.git
```

### Loading Embedding
```python
from Nepali_nlp import Embeddings
word_vec = Embeddings().load_large_vector()
#word_vec = Embeddings().load_vector() #For small Embedding
#from fasttext_embedding import Fasttext
#word_vec = Fasttext().load()
```

### For Nepali Synonym
```python
from Nepali_nlp import Synonym
Synonym().raw_synonym(word = 'माया',word_vec=word_vec) #method: 1
#output -> स्नेह','प्रेम','आदर','मायाँ','दया','मायालु','श्रद्धा','आत्मियता','स्पर्श','तिमी
Synonym().filter_synonym(word = 'साथी',word_vec=word_vec) #method: 2
#output -> 'भाइहरू','सहपाठी','प्रेमी','दाइ','प्रेमि','बहिनी'
```

### Word-spell corrector
```python
from Nepali_nlp import Corrector
Corrector().corrector(word='सुशल') #In a very raw stage for now.
#output-> ['सुशील', 'सुशील']
Corrector().spell_correct("कस्त भको हेरौ है")
#output-> "कस्तो भयो हेर है"
```

### Nepali text summarizer
```python
from Nepali_nlp import Summerize
Summerize().show_summary(word_vec, text, length_sentence_predict=5)
```

### Nepali unicode to Devnagari Font

```python
from Nepali_nlp import Unicode
text = 'ma ghara jaanchhu'
Unicode().unicode_word(text) #output-> 'म घर जान्छु'
```

### Preeti-font character to Devnagari Font
```python
from Nepali_nlp import preeti
unicode_word = 'g]kfnL'
print(preeti(unicode_word)) #output-> नेपाली
```

### OCR(optical character reader)
```python
from Nepali_nlp import OCR
text = OCR(image_location)
```

### Nepali Tokenizer
```python
from Nepali_nlp import Tokenizer
Tokenizer().sentence_tokenize(text) #To tokenize sentence
Tokenizer().word_tokenize(text) #To tokenize word
Tokenizer().character_tokenize(text) #To tokenize character
```

### Nepali Stemming

```python
from Nepali_nlp import Stem
text = "सरकारका प्रवक्ता प्रदीप ज्ञवालीले पनि गत बिहीबार उनलाई अनशन तोड्न आग्रह गरेका थिए" #str or list of word
Stem().rootify(text)
#output -> ['सरकार','प्रवक्ता','प्रदीप','ज्ञवाली','पनि','गत','बिहीबार','उन','अनशन','तोड्न','आग्रह','गर','']
```

### Nepali sentence similarity

```python
from Nepali_nlp import  Avg_vector_similar
sentences = ["कुपोषणकै कारण शारीरिक र मानसिक रुपमा कमजोर मात्र होइन, अकालमै ज्यान पनि गुमाउनुको परेको समाचार बग्रेल्ती सुन्न सकिन्छ","कर्णाली प्रदेश सामाजिक विकास मन्त्रालयले उपलब्ध गराएको तथ्यांकले कर्णालीमा प्रत्येक वर्ष जन्मिएका ५ वर्षमुनीका बालबालिका १ हजार जनामध्ये ५८ जनाले ज्यान गुमाउँदै आएको देखाएको छ"]
Avg_vector_similar().pair_similarity(word_vec, sentences) #output-> 0.6817289590835571
```

### Nepali new-portal Scrapper (onlinekhabar and ekantipur for now)
```python
from Nepali_nlp import extract_news
news_link = 'https://www.onlinekhabar.com/2019/12/821094'
title, news = extract_news(news_link) #onlinekhabar and ekantipur is supported at the moment.
```

### Show latest news summary
```python
from Nepali_nlp import UpdateNews
title, links, summerized_news = UpdateNews().show_latest(word_vec=word_vec,portal='onlinekhabar',number_of_news=5) #ekantipur portal is also supported
```

#### TODOs:
- [x] Nepali Embeddings 
- [x] Tokenizers (sentence, word, character) 
- [x] Stop Words
- [x] Nepali Words Collection 
- [x] Nepali Word synonym
- [x] Roman Nepali to Nepali
- [x] Nepali OCR
- [x] Summerization 
- [x] Pos_tag
- [x] Nepali stemming
- [x] Sentence similarity score
- [x] Spell correction
- [ ] Named Entity Recognition (Currently)
- [ ] Translation(Nepali<->English)
