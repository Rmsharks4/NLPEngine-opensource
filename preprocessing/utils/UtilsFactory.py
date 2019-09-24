from preprocessing.utils.ContractionsDictionary import ContractionsDictionary
from preprocessing.utils.EmailsDictionary import EmailsDictionary
from preprocessing.utils.FiguresDictionary import FiguresDictionary
from preprocessing.utils.PorterStemmer import PorterStemmer
from preprocessing.utils.PunctuationDictionary import PunctuationDictionary
from preprocessing.utils.SpellCheckerLib import SpellCheckerLib
from preprocessing.utils.SplitsDictionary import SplitsDictionary
from preprocessing.utils.StopWordsDictionary import StopWordsDictionary
from preprocessing.utils.WordnetLemmatizer import WordnetLemmatizer


class UtilsFactory:

    @staticmethod
    def get_utils(util_type):
        switcher = {
            ContractionsDictionary.__name__: ContractionsDictionary(),
            EmailsDictionary.__name__: EmailsDictionary(),
            FiguresDictionary.__name__: FiguresDictionary(),
            PorterStemmer.__name__: PorterStemmer(),
            PunctuationDictionary.__name__: PunctuationDictionary(),
            SpellCheckerLib.__name__: SpellCheckerLib(),
            SplitsDictionary.__name__: SplitsDictionary(),
            StopWordsDictionary.__name__: StopWordsDictionary(),
            WordnetLemmatizer.__name__: WordnetLemmatizer()
        }
        return switcher.get(util_type, '')
