from feature_engineering.bl.AbstractWordCouplesDialogueFeatureEngineerImpl import AbstractWordCouplesDialogueFeatureEngineerImpl


class SynonymsDialogueFeatureEngineerImpl(AbstractWordCouplesDialogueFeatureEngineerImpl):

    def get_couples(self, args):
        return args.name()
