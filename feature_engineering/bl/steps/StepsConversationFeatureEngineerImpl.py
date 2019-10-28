
from feature_engineering.bl.AbstractConversationFeatureEngineer import AbstractConversationFeatureEngineer


class StepsConversationFeatureEngineerImpl(AbstractConversationFeatureEngineer):

    def engineer_feature_operation(self, args):
        return self.steps(args)

    def steps(self, args):
        pass
