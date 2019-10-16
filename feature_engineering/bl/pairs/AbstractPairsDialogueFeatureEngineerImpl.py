import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from nltk.corpus import wordnet


class AbstractPairsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        for word in args:
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    self.get_pairs(lemma)

    @abc.abstractmethod
    def get_pairs(self, args):
        pass
