from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
from feature_engineering.bl.tags.POSTagsDialogueFeatureEngineerImpl import POSTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.ActsUtils import ActsUtils


class QWhDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        for x, y in args[POSTagsDialogueFeatureEngineerImpl.__name__]:
            if y == args[ActsUtils.__name__].wdt or \
                    y == args[ActsUtils.__name__].wp or \
                    y == args[ActsUtils.__name__].wps or \
                    y == args[ActsUtils.__name__].wrb:
                return args[ActsUtils.__name__].qwh
        return None
