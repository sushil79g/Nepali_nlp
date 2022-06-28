<h1>This projects aims to build a library for all the NLP processes for Nepali Language.</h1>

<h2>Getting the module</h2>

```bash
!pip install git+https://github.com/sushil79g/Nepali_nlp.git
```

<h3>Loading Embedding</h3>

```python
from Nepali_nlp import Embeddings
word_vec = Embeddings().load_large_vector()
#word_vec = Embeddings().load_vector() #For small Embedding
#from fasttext_embedding import Fasttext
#word_vec = Fasttext().load()
```

<h3>For Nepali Synonym</h3>

```python
from Nepali_nlp import Synonym
Synonym().raw_synonym(word = 'माया',word_vec=word_vec) #method: 1
#output -> स्नेह','प्रेम','आदर','मायाँ','दया','मायालु','श्रद्धा','आत्मियता','स्पर्श','तिमी
Synonym().filter_synonym(word = 'साथी',word_vec=word_vec) #method: 2
#output -> 'भाइहरू','सहपाठी','प्रेमी','दाइ','प्रेमि','बहिनी'
```
<h3>Word-spell corrector</h3>

```python
from Nepali_nlp import Corrector
Corrector().corrector(word='सुशल') #In a very raw stage for now.
#output-> ['सुशील', 'सुशील']
Corrector().spell_correct("कस्त भको हेरौ है")
#output-> "कस्तो भयो हेर है"
```
<h3>Nepali text summerizer</h3>

```python
from Nepali_nlp import Summerize
Summerize().show_summary(word_vec,text, length_sentence_predict=5)
```
<h3>Nepali unicode to Devnagiri Font</h3>

```python
from Nepali_nlp import Unicode
text = 'ma ghara jaanchhu'
Unicode().unicode_word(text) #output-> 'म घर जान्छु'
```
<h3>Preeti-font character to Devnagiri Font</h3>

```python
from Nepali_nlp import preeti
unicode_word = 'g]kfnL'
print(preeti(unicode_word)) #output-> नेपाली
```
<h3>OCR(optical character reader)</h3>

```python
from Nepali_nlp import OCR
text = OCR(image_location)
```
<h3>Nepali Tokenizer</h3>

```python
from Nepali_nlp import Tokenizer
Tokenizer().sentence_tokenize(text) #To tokenize sentence
Tokenizer().word_tokenize(text) #To tokenize word
Tokenizer().character_tokenize(text) #To tokenize character
Tokenizer().sentencepeice_tokenize(text) #Tokenize using BPE
```

<h3>Nepali Stemming</h3>

```python
from Nepali_nlp import Stem
text = "सरकारका प्रवक्ता प्रदीप ज्ञवालीले पनि गत बिहीबार उनलाई अनशन तोड्न आग्रह गरेका थिए" #str or list of word
Stem().rootify(text)
#output -> ['सरकार','प्रवक्ता','प्रदीप','ज्ञवाली','पनि','गत','बिहीबार','उन','अनशन','तोड्न','आग्रह','गर','']
```

<h3>Nepali sentence similarity</h3>

```python
from Nepali_nlp import  Avg_vector_similar
sentences = ["कुपोषणकै कारण शारीरिक र मानसिक रुपमा कमजोर मात्र होइन, अकालमै ज्यान पनि गुमाउनुको परेको समाचार बग्रेल्ती सुन्न सकिन्छ","कर्णाली प्रदेश सामाजिक विकास मन्त्रालयले उपलब्ध गराएको तथ्यांकले कर्णालीमा प्रत्येक वर्ष जन्मिएका ५ वर्षमुनीका बालबालिका १ हजार जनामध्ये ५८ जनाले ज्यान गुमाउँदै आएको देखाएको छ"]
Avg_vector_similar().pair_similarity(word_vec, sentences) #output-> 0.6817289590835571
```

<h3>Nepali new-portal Scrapper (onlinekhabar and ekantipur for now)</h3>

```python
from Nepali_nlp import extract_news
news_link = 'https://www.onlinekhabar.com/2019/12/821094'
title, news = extract_news(news_link) #onlinekhabar and ekantipur is supported at the moment.
```
<h3>Show latest news summary</h3>

```python
from Nepali_nlp import UpdateNews
title, links, summerized_news = UpdateNews().show_latest(word_vec=word_vec,portal='onlinekhabar',number_of_news=5) #ekantipur portal is also supported
```

<h3>Language Translation (English--Nepali)</h3>

```python
from Nepali_nlp import LanguageTranslation
conv = LanguageTranslation()
nepali_text = "प्रधानमन्त्री निवास बालुवाटारमा आज बिहान बसेको बैठकमा आसन्न स्थानीय तहको निर्वाचनको विषयमा छलफल भएको थियो । छलफलपछि सरकारका प्रवक्ता ज्ञानेन्द्रबहादुर कार्कीले निर्वाचन समयमै सम्पन्न गर्न आफूहरु सहमत भएको सन्चारकर्मीलाई जानकारी दिए ।"
english_text = "You already know that a data class is just a regular class. That means that you can freely add your own methods to a data class. As an example, let us calculate the distance between one position and another, along the Earth’s surface"

output = conv.to_nepali(english_text) #output-> ['तपाईँले पहिले नै जान्नु भएको छ कि डेटा वर्ग एउटा नियमित वर्ग मात्र हो । यसको अर्थ तपाईँले डेटा वर्गमा तपाईँको आफ्नै विधिहरू स्वतन्त्र रूपमा थप्न सक्नुहुन्छ । उदाहरणका लागि, हामीलाई पृथ्वीको सतहमा एक स्थान र अर्को बीचको दूरी गणना गर्नुहोस्']

output = conv.to_english(nepali_text) #output-> ['After the meeting, government spokesman Gyanendra Bahadur Patel informed the media that they agreed to hold elections on time.']
```

<h3> Language Transliteration </h3>

```python
from Nepali_nlp import Transliteration
engine = Transliteration()
engine.translit_word("Hello", topk=3)   # output -> ['हेल्लो', 'हेलो', 'हेललो']
engine.translit_sentence("Hey, Do you like programming?")   # output -> हे, डो योउ लाइक प्रोग्रामिङ?
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
- [x] Pos_tag
- [x] Nepali stemming
- [x] Sentence similarity score
- [x] Spell correction
- [x] Translation (Nepali<->English)
- [x] Transliteration 
- [ ] Named Entity Recognition (Currently)
