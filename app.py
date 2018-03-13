# see http://www.nltk.org/howto/wordnet.html
## install:

# sudo apt install libsqlite3-dev
# Y luego pyenv install 3.6.4 (order matters)
# python -m nltk.downloader all



from nltk.corpus import wordnet as wn
import pprint
from itertools import chain



# get all languages 
sorted(wn.langs())

input = input("Enter word to get hyponyms and hypernyms: ")
language = 'spa'
lista = []
words = wn.synsets(input, lang=language)
print(words)
pp = pprint.PrettyPrinter(indent=4)
for word in words:
  print(word.definition)
  lista.append({
    'id': word.name(), 
    'word': word.lemma_names(language), 
    'meaning': word.definition(),
    'hypernyms': [],
    'hyponyms:': []
  })
  for hyponym in word.hyponyms():
    

pp.pprint(lista)

## [Synset('dog.n.01'), Synset('rotter.n.01')]
# Deberíamos ya tener en synset "bueno" del picto ingles
wn.synset('dog.n.01').lemma_names('spa') # obtenemos can y perro
print ('hypernyms: ', wn.synset('dog.n.01').hypernyms())
print ('hyponyms: ',wn.synset('dog.n.01').hyponyms())

#for ss in wn.synsets('green'):
#    print(ss, ss.hypernyms())

for i,j in enumerate(wn.synset('dog.n.01').hypernyms()):
  print("Meaning",i, "NLTK ID:", j.lemma_names('spa'))
  #print( "Hypernyms:", ", ".join(list(chain(*[l.lemma_names for l in j.hypernyms()]))))
  #print("Hyponyms:", ", ".join(list(chain(*[l.lemma_names for l in j.hyponyms()]))))
  #print
