
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
import nltk


class PorterStemmerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__class__.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__class__.__name__]
        self.config_pattern.properties.req_args = None
        self.PorterStemmer = nltk.PorterStemmer()

    @classmethod
    def stem(cls, text):
        return cls.PorterStemmer.stem(text)

    @classmethod
    def preprocess_operation(cls, args):
        return [PorterStemmerDialoguePreProcessorImpl.stem(text) for text in args]
