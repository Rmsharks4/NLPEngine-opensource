import logging
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer


class AbstractDialogueFeatureEngineerFactory:

    @staticmethod
    def get_feature_engineer(feature_type):
        switcher = {
            # to be filled out when all classes complete
        }
        return switcher.get(feature_type, None)
