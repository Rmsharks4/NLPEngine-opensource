
from feature_engineering.bl.steps.StepsConversationFeatureEngineerImpl import StepsConversationFeatureEngineerImpl


class BackwardStepsConversationFeatureEngineerImpl(StepsConversationFeatureEngineerImpl):

    def steps(self, args):
        prev = None
        for intents in args:
            for intent in intents:
                if 'RESPONSE' in intent:
                    if prev is None or intent[:-(len(intent)-intent.find('_RESPONSE'))] not in prev:
                        intents.pop(intent)
            prev = intents
        return args
