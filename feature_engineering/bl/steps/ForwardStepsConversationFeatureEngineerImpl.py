
from feature_engineering.bl.steps.StepsConversationFeatureEngineerImpl import StepsConversationFeatureEngineerImpl


class ForwardStepsConversationFeatureEngineerImpl(StepsConversationFeatureEngineerImpl):

    def steps(self, args):
        prev = None
        for intents in args.reverse():
            for intent in intents:
                if intent == 'QWH' or intent == 'QYN':
                    if prev is not None and ['QWH', 'QYN'] not in prev:
                        intents.append('ANSW')
            prev = intents
        return args
