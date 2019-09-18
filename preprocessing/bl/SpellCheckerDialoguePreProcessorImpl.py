
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.bl.RemovePunctuationDialoguePreProcessorImpl import RemovePunctuationDialoguePreProcessorImpl
from spellchecker import SpellChecker

spell_checker = SpellChecker()


class SpellCheckerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = RemovePunctuationDialoguePreProcessorImpl.__class__.__name__
        self.config_pattern.properties.req_args = None

    @classmethod
    def spell_check(cls, text):
        return spell_checker.correction(text)

    @classmethod
    def preprocess_operation(cls, args):
        return [SpellCheckerDialoguePreProcessorImpl.spell_check(text) for text in args]
