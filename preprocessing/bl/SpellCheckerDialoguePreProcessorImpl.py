
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from spellchecker import SpellChecker

spell_checker = SpellChecker()


class SpellCheckerDialoguePreProcessorImpl(AbstractDialoguePreProcessor):

    @classmethod
    def spell_check(cls, text):
        return spell_checker.correction(text)

    @classmethod
    def preprocess_operation(cls, args):
        return [SpellCheckerDialoguePreProcessorImpl.spell_check(text) for text in args]
