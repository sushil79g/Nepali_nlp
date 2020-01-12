<h1>This projects aims to build a library for all the NLP processes for Nepali Language.</h1>

<h2>Getting the module</h2>

```bash
git clone git@github.com:sushil79g/Nepali_nlp.git
cd Nepali_nlp/nepali_nlp
```

<h3>Loading Embedding</h3>

```python
from Embedding import Embeddings
word_vec = Embeddings().load_vector()
#word_vec = Embeddings().load_large_vector() #For large Embedding
#from fasttext_embedding import Fasttext
#word_vec = Fasttext().load()
```

<h3>For Nepali Synonym</h3>

```python
from synonym import Synonym
Synonym().raw_synonym(word = 'माया',word_vec=word_vec) #method: 1
#output -> स्नेह','प्रेम','आदर','मायाँ','दया','मायालु','श्रद्धा','आत्मियता','स्पर्श','तिमी
Synonym().filter_synonym(word = 'साथी',word_vec=word_vec) #method: 2
#output -> 'भाइहरू','सहपाठी','प्रेमी','दाइ','प्रेमि','बहिनी'
```
<h3>Word-spell corrector</h3>

```python
from spellcheck import Corrector
Corrector().corrector(word='सुशल') #In a very raw stage for now.
#output-> ['सुशील', 'सुशील']
```
<h3>Nepali text summerizer</h3>

```python
from summerization import Summerize
Summerize().show_summary(word_vec,text, length_sentence_predict=5)
```
<h3>Nepali unicode to Devnagiri Font</h3>

```python
from unicode_nepali import Unicode
text = 'ma ghara jaanchhu'
Unicode().unicode_word(text) #output-> 'म घर जान्छु'
```
<h3>Preeti-font character to Devnagiri Font</h3>

```python
from preeti_unicode import preeti
unicode_word = 'g]kfnL'
print(preeti(unicode_word)) #output->'नेपाल'ी
```
<h3>OCR(optical character reader)</h3>

```python
from ocr import OCR
text = OCR(image_location)
```
<h3>Nepali Tokenizer</h3>

```python
from tokenize import Tokenizer
Tokenizer().sentence_tokenize(text) #To tokenize sentence
Tokenizer().word_tokenize(text) #To tokenize word
Tokenizer().character_tokenize(text) #To tokenize character
```

<h3>Nepali new-portal Scrapper (onlinekhabar and ekantipur for now)</h3>

```python
from news_scrap import extract_news
news_link = 'https://www.onlinekhabar.com/2019/12/821094'
title, news = extract_news(news_link) #onlinekhabar and ekantipur is supported at the moment.
```
<h3>Show latest news summary</h3>

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
