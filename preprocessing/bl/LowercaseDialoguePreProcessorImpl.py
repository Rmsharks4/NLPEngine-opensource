"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Lowercase**:
turns all characters to lowercase (CHAR to char, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl


class LowercaseDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Lowercase Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_data = [[SpellCheckerDialoguePreProcessorImpl.__name__]]
        self.config_pattern.properties.req_args = None

    @classmethod
    def lowercase(cls, text):
        """

        :param text: (str) string to examine
        :return: (str) preprocessed data
        """
        return text.lower()

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (list(str))
        (None)
        :return: (list) array of preprocessed data
        """
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.lowercase(args[req_data])
        return None
