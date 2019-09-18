
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
import nltk


class RemoveStopWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = SpellCheckerDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None
        self.stopwords = nltk.corpus.stopwords.words('english')

    @classmethod
    def remove_stop_words(cls, text):
        return text if text not in cls.stopwords else ''

    @classmethod
    def preprocess_operation(cls, args):
        return [RemoveStopWordsDialoguePreProcessorImpl.remove_stop_words(text) for text in args]
