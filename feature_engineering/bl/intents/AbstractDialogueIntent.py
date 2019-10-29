from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
from feature_engineering.utils.KeyProcessor import KeyProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl


class AbstractDialogueIntent(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [SpellCheckerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = KeyProcessor.__name__

    def intent(self, args):
        args[KeyProcessor.__name__].set_filename(self.__class__.__name__)
        return args[KeyProcessor.__name__].kp.extract_keywords(args[SpellCheckerDialoguePreProcessorImpl.__name__])
