from feature_engineering.utils.ActsUtils import ActsUtils
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer


class StepsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_args = ActsUtils.__name__

    def engineer_feature_operation(self, args):
        return self.steps(args)

    def steps(self, args):
        pass
