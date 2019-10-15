"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Plain Text**:
Input Sequence (raw)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor


class PlainTextDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Plain Text Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = []
        self.config_pattern.properties.req_args = None

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (list(str))
        (None)
        :return: (list) array of preprocessed data
        """
        pass
