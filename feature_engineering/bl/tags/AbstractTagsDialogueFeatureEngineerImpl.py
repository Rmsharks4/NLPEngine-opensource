import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from feature_engineering.utils.SpacyModel import SpacyModel


class AbstractTagsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [SpellCheckerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = SpacyModel.__name__

    def engineer_feature_operation(self, args):
        return self.tags(args[SpacyModel.__name__].nlp(args[SpellCheckerDialoguePreProcessorImpl.__name__]))

    @abc.abstractmethod
    def tags(self, args):
        pass
