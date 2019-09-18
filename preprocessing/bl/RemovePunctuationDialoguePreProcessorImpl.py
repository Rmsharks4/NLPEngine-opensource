
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl
import string


class RemovePunctuationDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemoveEmailsDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None

    @classmethod
    def remove_punctuation(cls, text):
        return "".join([char for char in text if char not in string.punctuation])

    @classmethod
    def preprocess_operation(cls, args):
        return [RemovePunctuationDialoguePreProcessorImpl.remove_punctuation(text) for text in args]