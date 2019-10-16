from feature_engineering.bl.pairs.AbstractPairsDialogueFeatureEngineerImpl import AbstractPairsDialogueFeatureEngineerImpl


class AntonymsDialogueFeatureEngineerImpl(AbstractPairsDialogueFeatureEngineerImpl):

    def get_pairs(self, args):
        if args.antonyms():
            return args.antonyms()[0].name()
        else:
            return None
