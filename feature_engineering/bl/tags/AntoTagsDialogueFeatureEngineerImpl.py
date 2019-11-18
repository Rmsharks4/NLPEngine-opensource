from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
from nltk.corpus import wordnet
import nltk


class AntoTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[AbstractTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = None

    @staticmethod
    def antonyms(token):
        antonyms = []
        for syn in wordnet.synsets(str(token)):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
        return antonyms

    def tags(self, args):
        return [(token, self.antonyms(token)) for token in args if self.antonyms(token) != []]
