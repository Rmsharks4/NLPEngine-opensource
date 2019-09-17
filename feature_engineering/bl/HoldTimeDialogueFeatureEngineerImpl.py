from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.utils.MathematicsUtils import MathematicsUtils


class HoldTimeDialogueFeatureEngineer(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        hold_time = MathematicsUtils.subtract([args[1], args[0]])
        return MathematicsUtils.set_value([hold_time, 0, 0, '<'])
