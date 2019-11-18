from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
from nltk.corpus import wordnet


class SynTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[AbstractTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = None

    @staticmethod
    def synonyms(token):
        synonyms = []
        for syn in wordnet.synsets(str(token)):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return synonyms

    def tags(self, args):
        return [(token, self.synonyms(token)) for token in args if self.synonyms(token) != []]
