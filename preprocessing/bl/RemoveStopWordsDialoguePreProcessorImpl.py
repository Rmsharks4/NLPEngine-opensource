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
from preprocessing.bl.LowercaseDialoguePreProcessorImpl import LowercaseDialoguePreProcessorImpl
from preprocessing.utils.StopWordsDictionary import StopWordsDictionary
import re


class RemoveStopWordsDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Stop Words Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_data = [[LowercaseDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = StopWordsDictionary.__name__

    @classmethod
    def remove_stop_words(cls, text, stopwords):
        """

        :param text: (str) string to examine
        :param stopwords: (StopWordsDictionary) stop words utils
        :return: (str) preprocessed data
        """
        return ''.join(x+' ' if x not in stopwords.stopwords_dict else stopwords.stopwords_replace for x in re.split('[\s,]+', text))

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (SpellCheckerDialoguePreProcessorImpl)
        (StopWordsDictionary)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.remove_stop_words(args[req_data], args[self.config_pattern.properties.req_args])
        return None
