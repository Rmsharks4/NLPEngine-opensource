
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class LowercaseDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_args = None

    @classmethod
    def lowercase(cls, text):
        return text.lower()

    def preprocess_operation(self, args):
        return [self.lowercase(args[self.config_pattern.properties.req_data])]
