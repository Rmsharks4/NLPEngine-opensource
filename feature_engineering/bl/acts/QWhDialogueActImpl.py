from feature_engineering.bl.acts.AbstractDialogueAct import AbstractDialogueAct
from feature_engineering.bl.tags.POSTagsDialogueFeatureEngineerImpl import POSTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.ActsUtils import ActsUtils


class QWhDialogueActImpl(AbstractDialogueAct):

    def act(self, args):
        for y in args[POSTagsDialogueFeatureEngineerImpl.__name__]:
            if str(y[1]) == args[ActsUtils.__name__].wdt or \
                    str(y[1]) == args[ActsUtils.__name__].wp or \
                    str(y[1]) == args[ActsUtils.__name__].wps or \
                    str(y[1]) == args[ActsUtils.__name__].wrb:
                return args[ActsUtils.__name__].qwh
        return None
