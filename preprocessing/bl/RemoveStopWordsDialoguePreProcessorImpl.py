
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.utils.StopWordsDictionary import StopWordsDictionary


class RemoveStopWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = SpellCheckerDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = StopWordsDictionary.__class__.__name__

    @classmethod
    def remove_stop_words(cls, text, stopwords):
        return text if text not in stopwords.stopwrods_dict else stopwords.stopwords_replace

    def preprocess_operation(self, args):
        return [self.remove_stop_words(args[self.config_pattern.properties.req_data],
                                       args[self.config_pattern.properties.req_args])]
