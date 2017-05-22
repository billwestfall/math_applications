import nltk
from nltk.parse.generate import generate
from nltk import CFG

f=open('thesaurus.txt','rU')
raw=f.read()
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
grammar = CFG.fromstring(text)
for sentence in generate(grammar, n=10): print(' '.join(sentence))
