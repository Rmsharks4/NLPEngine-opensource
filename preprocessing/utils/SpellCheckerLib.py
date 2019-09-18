from spellchecker import SpellChecker


class SpellCheckerLib:

    spell_checker_lib = None

    @staticmethod
    def load():
        SpellCheckerLib.spell_checker_lib = SpellChecker()
