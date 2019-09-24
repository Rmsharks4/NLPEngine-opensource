from preprocessing.utils.UtilsFactory import UtilsFactory


class SplitsDictionary(UtilsFactory):

    splits_dict = None
    splits_replace = None

    @staticmethod
    def load():
        SplitsDictionary.splits_dict = ['-', '_']
        SplitsDictionary.splits_replace = ' '
