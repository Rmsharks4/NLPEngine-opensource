"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class operates on one static function
- load (loads the static object required for preprocesing)

**Spell Checker**:
downloads spell checker from Spell Checker lib

"""

from spellchecker import SpellChecker
from preprocessing.utils.UtilsFactory import UtilsFactory


class SpellCheckerLib(UtilsFactory):

    spell_checker_lib = None

    @staticmethod
    def load():
        SpellCheckerLib.spell_checker_lib = SpellChecker()
