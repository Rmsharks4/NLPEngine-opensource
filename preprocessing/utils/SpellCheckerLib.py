from spellchecker import SpellChecker
from preprocessing.utils.UtilsFactory import UtilsFactory


class SpellCheckerLib(UtilsFactory):

    spell_checker_lib = None

    @staticmethod
    def load():
        SpellCheckerLib.spell_checker_lib = SpellChecker()
