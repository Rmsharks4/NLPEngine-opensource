"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Remove Punctuation**:
remove all punctuation from text (a,b,c to a b c)

"""

from preprocessing.utils.PunctuationDictionary import PunctuationDictionary
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemoveEmailsDialoguePreProcessorImpl import RemoveEmailsDialoguePreProcessorImpl


class RemovePunctuationDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Punctuation Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = RemoveEmailsDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = PunctuationDictionary.__name__

    @classmethod
    def remove_punctuation(cls, text, punctuation):
        """

        :param text: (str) string to examine
        :param punctuation: (PunctuationDictionary) punctuation utils
        :return: (str) preprocessed data
        """
        return punctuation.punctuation_replace.join([char for char in text if char not in punctuation.punctuation_dict])

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (RemoveEmailsDialoguePreProcessorImpl)
        (PunctuationDictionary)
        :return: (list) array of preprocessed data
        """
        return self.remove_punctuation(args[self.config_pattern.properties.req_data],
                                        args[self.config_pattern.properties.req_args])
