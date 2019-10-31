from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
from feature_engineering.bl.tags.POSTagsDialogueFeatureEngineerImpl import POSTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.ActsUtils import ActsUtils


class ImpDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        if len(args[POSTagsDialogueFeatureEngineerImpl.__name__]) > 0:
            x, y = args[POSTagsDialogueFeatureEngineerImpl.__name__].values[0]
            if y == args[ActsUtils.__name__].vb:
                return args[ActsUtils.__name__].imp
        return None
