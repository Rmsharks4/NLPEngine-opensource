from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
from nltk.corpus import wordnet
import nltk


class NLTKTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    @staticmethod
    def synonyms(token):
        synonyms = []
        for syn in wordnet.synsets(token):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return synonyms

    @staticmethod
    def antonyms(token):
        antonyms = []
        for syn in wordnet.synsets(token):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        return antonyms

    def tags(self, args):
        return [{
            'Token': token,
            'Stem': nltk.PorterStemmer().stem(token),
            'Lemma': nltk.WordNetLemmatizer().lemmatize(token, pos='v'),
            'Stop': True if token in nltk.corpus.stopwords.words('english') else False,
            'Syn': self.synonyms(token),
            'Anto': self.antonyms(token),
            'POS': nltk.pos_tag(token),
            'NER': nltk.ne_chunk(token),
            'IOB': nltk.tree2conlltags(token)
            } for token in nltk.word_tokenize(args)]
