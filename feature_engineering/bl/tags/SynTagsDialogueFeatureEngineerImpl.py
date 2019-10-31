from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
from nltk.corpus import wordnet


class SynTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    @staticmethod
    def synonyms(token):
        synonyms = []
        for syn in wordnet.synsets(str(token)):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return synonyms

    def tags(self, args):
        return [(token, self.synonyms(token)) for token in args]
