This projects aims to build a library for all the NLP processes for Nepali Language.

TODOs:</br>
- [x] Nepali Embeddings 
- [x] Tokenizers (sentence, word, character) 
- [x] Stop Words
- [x] Nepali Words Collection 
- [x] Nepali Word synonym
- [x] Roman Nepali to Nepali
- [ ] Spell correction (Currently)
- [ ] Word and sentence similarity score
- [ ] Pos_tag
- [x] Summerization 
- [ ] Named Entity Recognition
- [x] Nepali OCR


Loading Embedding
```python
from Embedding import Embeddings
word_vec = Embeddings().load_vector()
#word_vec = Embeddings().load_large_vector() #For large Embedding
#from fasttext_embedding import Fasttext
#word_vec = Fasttext().load()
```
