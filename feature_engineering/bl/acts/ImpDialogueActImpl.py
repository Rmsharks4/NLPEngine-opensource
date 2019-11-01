from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
from feature_engineering.bl.tags.POSTagsDialogueFeatureEngineerImpl import POSTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.ActsUtils import ActsUtils


class ImpDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        y = args[POSTagsDialogueFeatureEngineerImpl.__name__][0]
        if str(y[1]) == args[ActsUtils.__name__].vb:
            return args[ActsUtils.__name__].imp
        return None
