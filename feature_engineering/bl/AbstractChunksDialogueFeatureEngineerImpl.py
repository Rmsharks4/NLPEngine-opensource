import abc
from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer


class AbstractChunksDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def engineer_feature_operation(self, args):
        return self.chunks(args)

    @abc.abstractmethod
    def chunks(self, args):
        pass
