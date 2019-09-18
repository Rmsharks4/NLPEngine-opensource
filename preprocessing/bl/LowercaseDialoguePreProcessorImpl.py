
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class LowercaseDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_args = None

    @classmethod
    def lowercase(cls, text):
        return text.lower()

    @classmethod
    def preprocess_operation(cls, args):
        return [LowercaseDialoguePreProcessorImpl.lowercase(text) for text in args]