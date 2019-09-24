
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveStopWordsDialoguePreProcessorImpl import RemoveStopWordsDialoguePreProcessorImpl
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.utils.PorterStemmer import PorterStemmer


class PorterStemmerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [RemoveStopWordsDialoguePreProcessorImpl.__name__,
                                                   SpellCheckerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = PorterStemmer.__name__

    @classmethod
    def stem(cls, text, stemmer):
        return stemmer.stemmer_lib.stem(text)

    def preprocess_operation(self, args):
        return [self.stem(args[self.config_pattern.properties.req_data],
                          args[self.config_pattern.properties.req_args])]
