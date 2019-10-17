
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

texts = 'Welcome to Australia Post Load and Go Support my name is Archie may I please have your card number.'

doc = nlp(texts)
print(displacy.serve(doc))

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)
