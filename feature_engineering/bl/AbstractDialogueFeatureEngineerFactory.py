import logging
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from preprocessing.bl import *
from feature_engineering.bl.intents import *
from feature_engineering.bl.tags import *
from feature_engineering.bl.intents import *
from feature_engineering.bl.difficulty_index import *
from feature_engineering.bl.acts import *
from feature_engineering.bl.NGramsDialogueFeatureEngineerImpl import NGramsDialogueFeatureEngineerImpl
from feature_engineering.bl.WordsPerMinuteDialogueFeatureEngineerImpl import WordsPerMinuteDialogueFeatureEngineerImpl


class AbstractDialogueFeatureEngineerFactory:

    @staticmethod
    def get_feature_engineer(feature_type):
        switcher = dict()
        for y in AbstractDialogueFeatureEngineer().__class__.__subclasses__():
            switcher[y.__name__] = y()
            switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))
        return switcher.get(feature_type, None)
