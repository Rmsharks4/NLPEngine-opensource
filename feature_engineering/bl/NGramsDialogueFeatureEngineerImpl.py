from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer


class NGramsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        return zip(*[args[0][i:] for i in range(args[1])])
