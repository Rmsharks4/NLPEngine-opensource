
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
import string


class RemovePunctuationDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def remove_punctuation(cls, text):
        return "".join([char for char in text if char not in string.punctuation])

    @classmethod
    def preprocess_operation(cls, args):
        return [RemovePunctuationDialoguePreProcessorImpl.remove_punctuation(text) for text in args]