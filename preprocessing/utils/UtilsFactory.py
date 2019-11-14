"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class selects which file implementation should be used at any given time.
- get_utils (takes class name as argument)
"""

from preprocessing.utils.ContractionsDictionary import ContractionsDictionary
from preprocessing.utils.EmailsDictionary import EmailsDictionary
from preprocessing.utils.FiguresDictionary import FiguresDictionary
from preprocessing.utils.PunctuationDictionary import PunctuationDictionary
from preprocessing.utils.SplitsDictionary import SplitsDictionary
from preprocessing.utils.StopWordsDictionary import StopWordsDictionary
from preprocessing.utils.WordnetLemmatizer import WordnetLemmatizer


class UtilsFactory:

    @staticmethod
    def get_utils(util_type):
        """

        :param util_type: (AbstractUtils) class name
        :return: (AbstractUtils) object else throws Exception
        """
        switcher = {
            ContractionsDictionary.__name__: ContractionsDictionary(),
            EmailsDictionary.__name__: EmailsDictionary(),
            FiguresDictionary.__name__: FiguresDictionary(),
            PunctuationDictionary.__name__: PunctuationDictionary(),
            SplitsDictionary.__name__: SplitsDictionary(),
            StopWordsDictionary.__name__: StopWordsDictionary(),
            WordnetLemmatizer.__name__: WordnetLemmatizer()
        }
        return switcher.get(util_type, None)
