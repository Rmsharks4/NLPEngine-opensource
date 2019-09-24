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


class SpellCheckerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemovePunctuationDialoguePreProcessorImpl.__name__
        self.config_pattern.properties.req_args = SpellCheckerLib.__name__

    @classmethod
    def spell_check(cls, text, spell_checker):
        return spell_checker.spell_checker_lib.correction(text)

    def preprocess_operation(self, args):
        return [self.spell_check(args[self.config_pattern.properties.req_data],
                                 args[self.config_pattern.properties.req_args])]
