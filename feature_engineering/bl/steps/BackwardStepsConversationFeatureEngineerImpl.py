
from feature_engineering.bl.steps.StepsConversationFeatureEngineerImpl import StepsConversationFeatureEngineerImpl


class BackwardStepsConversationFeatureEngineerImpl(StepsConversationFeatureEngineerImpl):

    def steps(self, args):
        prev = None
        for intents in args:
            dels = []
            for intent in intents:
                if 'RESPONSE' in intent:
                    if self.prev_match(intent[:-(len(intent) - intent.find('_RESPONSE'))], prev):
                        dels.append(intent)
            for delin in dels:
                intents.remove(delin)
            prev = intents
        return args

    def prev_match(self, match, arr):
        look = False
        for prevint in arr:
            if match in prevint and 'RESPONSE' not in prevint:
                look = True
        if look:
            return False
        return True
