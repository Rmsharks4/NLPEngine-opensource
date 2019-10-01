"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Remove Numeric Characters**:
remove all digits and alike (14, fourteen, sunday, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.ExpandContractionsDialoguePreProcessorImpl import ExpandContractionsDialoguePreProcessorImpl
from preprocessing.utils.FiguresDictionary import FiguresDictionary


class RemoveNumericCharactersDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Remove Numeric Characters Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = ExpandContractionsDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = FiguresDictionary.__name__

    @classmethod
    def remove_numeric_characters(cls, text, figures):
        """

        :param text: (str) string to examine
        :param figures: (FiguresDictionary) figures utils
        :return: (str) preprocessed data
        """
        def replace(match):
            return figures.figures_dict[match.group(0)]
        text = figures.numbers_re.sub(figures.replace_text, text)
        return figures.figures_re.sub(replace, text)
        
    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (ExpandContractionsDialoguePreProcessorImpl)
        (FiguresDictionary)
        :return: (list) array of preprocessed data
        """
        return self.remove_numeric_characters(args[self.config_pattern.properties.req_data],
                                               args[self.config_pattern.properties.req_args])
