from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils
from data.bl.StartTimeDataImpl import StartTimeDataImpl
from data.bl.EndTimeDataImpl import EndTimeDataImpl


class HoldTimeDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = None
        self.config_pattern.properties.req_input = [[StartTimeDataImpl.__name__, EndTimeDataImpl.__name__]]
        self.config_pattern.properties.req_args = None

    def engineer_feature_operation(self, args):
        args[EndTimeDataImpl.__name__].drop(args[EndTimeDataImpl.__name__].tail(1).index, inplace=True)
        args[EndTimeDataImpl.__name__].loc[-1] = 0
        args[EndTimeDataImpl.__name__].index = args[EndTimeDataImpl.__name__].index + 1
        args[EndTimeDataImpl.__name__] = args[EndTimeDataImpl.__name__].sort_index()
        args[StartTimeDataImpl.__name__] = args[StartTimeDataImpl.__name__].apply(
            lambda x: int(x))
        args[EndTimeDataImpl.__name__] = args[EndTimeDataImpl.__name__].apply(
            lambda x: int(x))
        return MathematicsUtils.subtract([args[StartTimeDataImpl.__name__],
                                          args[EndTimeDataImpl.__name__]]).apply(
            lambda x: MathematicsUtils.set_value([x, 0, 0, '<']))
