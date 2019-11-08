from feature_engineering.utils.ActsUtils import ActsUtils
from feature_engineering.bl.steps.StepsDialogueFeatureEngineerImpl import StepsDialogueFeatureEngineerImpl
from feature_engineering.bl.intents import *
from feature_engineering.bl.intents.AbstractDialogueIntent import AbstractDialogueIntent


class BackwardStepsDialogueFeatureEngineerImpl(StepsDialogueFeatureEngineerImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[x.__name__ for x in AbstractDialogueIntent.__subclasses__()]]

    def steps(self, args):
        res = None
        for req_data in self.config_pattern.properties.req_data:
            for data in req_data:
                if data in args:
                    if res is None:
                        res = [None] * len(args[data])
                    BackwardStepsDialogueFeatureEngineerImpl.stepdown({
                        data: args[data],
                        ActsUtils.__name__: args[ActsUtils.__name__]
                    }, data, res)
        return res

    @staticmethod
    def stepdown(args, name, res):
        i = 0
        dels = []
        prev = None
        for intents in args[name]:
            if intents is not None and args[ActsUtils.__name__].resp in intents:
                if BackwardStepsDialogueFeatureEngineerImpl.prev_match(
                        intents[:-(len(intents) - intents.find(args[ActsUtils.__name__].resp))],
                        prev, args[ActsUtils.__name__].resp):
                    dels.append(intents)
            if res[i] is None:
                res[i] = [intent for intent in intents if intent not in dels]
            else:
                res[i].extend([intent for intent in intents if intent not in dels])
            i += 1
            prev = intents

    @staticmethod
    def prev_match(match, arr, resp):
        look = False
        for prevint in arr:
            if match in prevint and resp not in prevint:
                look = True
        if look:
            return False
        return True
