import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from nltk.corpus import wordnet


class AbstractWordCouplesDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        for word in args:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    self.get_couples(lemma)

    @abc.abstractmethod
    def get_couples(self, args):
        pass
