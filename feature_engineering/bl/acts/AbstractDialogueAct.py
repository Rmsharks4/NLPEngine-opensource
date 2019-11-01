from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.tags.POSTagsDialogueFeatureEngineerImpl import POSTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.ActsUtils import ActsUtils


class AbstractDialogueAct(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[POSTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_args = ActsUtils.__name__

    def engineer_feature_operation(self, args):
        return args[POSTagsDialogueFeatureEngineerImpl.__name__].apply(
            lambda x: self.act({
                POSTagsDialogueFeatureEngineerImpl.__name__: x,
                ActsUtils.__name__: args[ActsUtils.__name__]}))

    def act(self, args):
        pass
