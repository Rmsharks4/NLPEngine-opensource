from feature_engineering.utils.ActsUtils import ActsUtils
from feature_engineering.bl.steps.StepsConversationFeatureEngineerImpl import StepsConversationFeatureEngineerImpl


class BackwardStepsConversationFeatureEngineerImpl(StepsConversationFeatureEngineerImpl):

    def steps(self, args):
        prev = None
        for intents in args:
            dels = []
            for intent in intents:
                if args[ActsUtils.__name__].resp in intent:
                    if self.prev_match(intent[:-(len(intent) - intent.find(args[ActsUtils.__name__].resp))],
                                       prev, args[ActsUtils.__name__].resp):
                        dels.append(intent)
            for delin in dels:
                intents.remove(delin)
            prev = intents
        return args

    @staticmethod
    def prev_match(match, arr, resp):
        look = False
        for prevint in arr:
            if match in prevint and resp not in prevint:
                look = True
        if look:
            return False
        return True
