"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Remove Stop Words**:
remove all frequently occurring words (the, by, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.utils.StopWordsDictionary import StopWordsDictionary


class RemoveStopWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Stop Words Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = SpellCheckerDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = StopWordsDictionary.__name__

    @classmethod
    def remove_stop_words(cls, text, stopwords):
        """

        :param text: (str) string to examine
        :param stopwords: (StopWordsDictionary) stop words utils
        :return: (str) preprocessed data
        """
        return text if text not in stopwords.stopwrods_dict else stopwords.stopwords_replace

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (SpellCheckerDialoguePreProcessorImpl)
        (StopWordsDictionary)
        :return: (list) array of preprocessed data
        """
        return [self.remove_stop_words(args[self.config_pattern.properties.req_data],
                                       args[self.config_pattern.properties.req_args])]
