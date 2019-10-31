from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.KeyProcessor import KeyProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl


class AbstractDialogueIntent(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[SpellCheckerDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = KeyProcessor.__name__

    def engineer_feature_operation(self, args):
        return self.intent(args)

    def intent(self, args):
        args[KeyProcessor.__name__].set_filename(self.__class__.__name__)
        return args[KeyProcessor.__name__].kp.extract_keywords(str(args[SpellCheckerDialoguePreProcessorImpl.__name__]))
