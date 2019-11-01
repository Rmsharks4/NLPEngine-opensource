from feature_engineering.utils.ActsUtils import ActsUtils
from feature_engineering.bl.steps.StepsDialogueFeatureEngineerImpl import StepsDialogueFeatureEngineerImpl


class ForwardStepsDialogueFeatureEngineerImpl(StepsDialogueFeatureEngineerImpl):

    def steps(self, args):
        # prev = None
        # for intents in args.reverse():
        #     for intent in intents:
        #         if intent == args[ActsUtils.__name__].qwh or intent == args[ActsUtils.__name__].qyn:
        #             if prev is not None and [args[ActsUtils.__name__].qwh,
        #                                      args[ActsUtils.__name__].qyn] not in prev:
        #                 intents.append(args[ActsUtils.__name__].answ)
        #     prev = intents
        # return args
        return None
