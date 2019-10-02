"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one major function:
- preprocess (operation and validation included!)

**Spell Checker**:
corrects spellings of words (cactos to cactus, etc.)

"""

from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from preprocessing.utils.SpellCheckerLib import SpellCheckerLib
import re


class SpellCheckerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        """
        initializes Spell Checker Dialogue Pre-Processor Class: set required data and arguments
        """
        super().__init__()
        self.config_pattern.properties.req_data = RemovePunctuationDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = SpellCheckerLib.__name__

    @classmethod
    def spell_check(cls, text, spell_checker):
        """

        :param text: (str) string to examine
        :param spell_checker: (SpellCheckerLib) spell checker utils
        :return: (str) preprocessed data
        """
        return ' '.join(spell_checker.spell_checker_lib.correction(x) if x != '' else x for x in re.split('[\s,]+', text))

    def preprocess_operation(self, args):
        """

        :param args: (dict) contains req_data and req_args
        (RemovePunctuationDialoguePreProcessorImpl)
        (SpellCheckerLib)
        :return: (list) array of preprocessed data
        """
        return self.spell_check(args[self.config_pattern.properties.req_data],
                                 args[self.config_pattern.properties.req_args])
