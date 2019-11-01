import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from feature_engineering.utils.SpacyModel import SpacyModel


class AbstractTagsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[RemovePunctuationDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = SpacyModel.__name__

    def engineer_feature_operation(self, args):
        return args[RemovePunctuationDialoguePreProcessorImpl.__name__].apply(
            lambda x: self.tags(args[SpacyModel.__name__].nlp(str(x))))

    def tags(self, args):
        pass
