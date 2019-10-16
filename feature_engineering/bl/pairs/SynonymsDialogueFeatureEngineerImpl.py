from feature_engineering.bl.pairs.AbstractPairsDialogueFeatureEngineerImpl import AbstractPairsDialogueFeatureEngineerImpl


class SynonymsDialogueFeatureEngineerImpl(AbstractPairsDialogueFeatureEngineerImpl):

    def get_pairs(self, args):
        return args.name()
