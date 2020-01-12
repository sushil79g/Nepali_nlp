This projects aims to build a library for all the NLP processes for Nepali Language.

Loading Embedding
```python
from Embedding import Embeddings
word_vec = Embeddings().load_vector()
#word_vec = Embeddings().load_large_vector() #For large Embedding
#from fasttext_embedding import Fasttext
#word_vec = Fasttext().load()
```

For Nepali Synonym
```python
from synonym import Synonym
Synonym().raw_synonym(word = 'माया',word_vec=word_vec) #method: 1
#output -> स्नेह','प्रेम','आदर','मायाँ','दया','मायालु','श्रद्धा','आत्मियता','स्पर्श','तिमी
Synonym().filter_synonym(word = 'साथी',word_vec=word_vec) #method: 2
#output -> 'भाइहरू','सहपाठी','प्रेमी','दाइ','प्रेमि','बहिनी'
```
Word-spell corrector
```python
from spellcheck import Corrector
Corrector().corrector(word='सुशल') #In a very raw stage for now.
#output-> ['सुशील', 'सुशील']
```
Nepali text summerizer
```python
from summerization import Summerize
Summerize().show_summary(word_vec,news, length_sentence_predict=5)
```
Nepali unicode to Devnagiri Font
```python
from unicode_nepali import Unicode
text = 'ma ghara jaanchhu'
Unicode().unicode_word(text) #output-> 'म घर जान्छु'
```
Preeti-font character to Devnagiri Font
```python
from preeti_unicode import preeti
unicode_word = 'g]kfnL'
print(preeti(unicode_word)) #output->'नेपाल'ी
```
OCR(optical character reader)
```python
from ocr import OCR
text = OCR(image_location)
```
Nepali new-portal Scrapper (onlinekhabar and ekantipur for now)
```python
from news_scrap import extract_news
news_link = 'https://www.onlinekhabar.com/2019/12/821094'
title, news = extract_news(news_link) #onlinekhabar and ekantipur is supported at the moment.
```
show latest news summary
```python
from news_latest import Update_news
title, links, summerized_news = Update_news().show_latest(word_vec=word_vec,portal='onlinekhabar',number_of_news=5) #ekantipur portal is also supported
```

TODOs:</br>
- [x] Nepali Embeddings 
- [x] Tokenizers (sentence, word, character) 
- [x] Stop Words
- [x] Nepali Words Collection 
- [x] Nepali Word synonym
- [x] Roman Nepali to Nepali
- [x] Nepali OCR
- [x] Summerization 
- [ ] Spell correction (Currently)
- [ ] Word and sentence similarity score
- [ ] Pos_tag
- [ ] Named Entity Recognition
