
from feature_engineering.utils.AbstractUtils import AbstractUtils


class WPMLimit(AbstractUtils):

    wpm = None

    @staticmethod
    def load():
        WPMLimit.wpm = 60
