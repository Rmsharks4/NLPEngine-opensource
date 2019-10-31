from feature_engineering.bl.AbstractConversationFeatureEngineer import AbstractConversationFeatureEngineer
from feature_engineering.bl.steps import *
from feature_engineering.bl.HoldTimeConversationFeatureEngineerImpl import HoldTimeDialogueFeatureEngineer


class AbstractConversationFeatureEngineerFactory:

    @staticmethod
    def get_feature_engineer(feature_type):
        switcher = dict()
        for y in AbstractConversationFeatureEngineer().__class__.__subclasses__():
            switcher[y.__name__] = y()
            switcher.update(dict((x.__name__, x()) for x in switcher[y.__name__].__class__.__subclasses__()))
        return switcher.get(feature_type, None)


