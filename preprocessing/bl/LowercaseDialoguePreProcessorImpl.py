
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class LowercaseDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def lowercase(cls, text):
        return text.lower()

    @classmethod
    def preprocess_operation(cls, args):
        return [LowercaseDialoguePreProcessorImpl.lowercase(text) for text in args]