from feature_engineering.utils.ActsUtils import ActsUtils
from feature_engineering.bl.steps.StepsDialogueFeatureEngineerImpl import StepsDialogueFeatureEngineerImpl
from feature_engineering.bl.acts.QWhDialogueActImpl import QWhDialogueActImpl
from feature_engineering.bl.acts.QYnDialogueActImpl import QYnDialogueActImpl


class ForwardStepsDialogueFeatureEngineerImpl(StepsDialogueFeatureEngineerImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[QWhDialogueActImpl.__name__, QYnDialogueActImpl.__name__]]

    def steps(self, args):
        res = None
        for req_data in self.config_pattern.properties.req_data:
            for data in req_data:
                if data in args:
                    if res is None:
                        res = [None] * len(args[data])
                    ForwardStepsDialogueFeatureEngineerImpl.stepup({
                        data: args[data],
                        ActsUtils.__name__: args[ActsUtils.__name__]
                    }, data, res)
        return res

    @staticmethod
    def stepup(args, name, res):
        i = 0
        prev = None
        for intents in args[name]:
            if intents is not None and (
                    intents == args[ActsUtils.__name__].qwh or intents == args[ActsUtils.__name__].qyn):
                if prev is not None and (
                        args[ActsUtils.__name__].qwh not in prev or args[ActsUtils.__name__].qyn not in prev):
                    res[i] = args[ActsUtils.__name__].answ
            i += 1
            prev = intents
