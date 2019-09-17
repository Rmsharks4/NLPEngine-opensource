from feature_engineering.bl.AbstractWordCouplesDialogueFeatureEngineerImpl import AbstractWordCouplesDialogueFeatureEngineerImpl


class AntonymsDialogueFeatureEngineerImpl(AbstractWordCouplesDialogueFeatureEngineerImpl):

    def get_couples(self, args):
        if args.antonyms():
            return args.antonyms()[0].name()
        else:
            return None
