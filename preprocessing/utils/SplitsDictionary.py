
class SplitsDictionary:

    splits_dict = None
    splits_replace = None

    @staticmethod
    def load():
        SplitsDictionary.splits_dict = ['-', '_']
        SplitsDictionary.splits_replace = ' '
