import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from feature_engineering.utils.SpacyModel import SpacyModel


class AbstractTagsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[SpellCheckerDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = SpacyModel.__name__

    def engineer_feature_operation(self, args):
        return self.tags(args[SpacyModel.__name__].nlp(str(args[SpellCheckerDialoguePreProcessorImpl.__name__])))

    def tags(self, args):
        pass
