
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from preprocessing.utils.SpellCheckerLib import SpellCheckerLib


class SpellCheckerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemovePunctuationDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = SpellCheckerLib.__class__.__name__

    @classmethod
    def spell_check(cls, text, spell_checker):
        return spell_checker.spell_checker_lib.correction(text)

    def preprocess_operation(self, args):
        return [self.spell_check(args[self.config_pattern.properties.req_data],
                                 args[self.config_pattern.properties.req_args])]
