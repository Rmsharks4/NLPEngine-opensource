from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer


class AbstractDialogueAct(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        return self.act(args)

    def act(self, args):
        pass
