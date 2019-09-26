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


class LowercaseDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Lowercase Dialogue Pre-Processor Class: set required data and arguments
        """
        self.logger.info('Calling Parent Constructor: ' + super.__class__.__name__)
        super().__init__()
        self.config_pattern.properties.req_data = None
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
        return [self.lowercase(args[self.config_pattern.properties.req_data])]
