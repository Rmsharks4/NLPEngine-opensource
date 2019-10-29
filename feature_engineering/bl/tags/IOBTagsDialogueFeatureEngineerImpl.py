from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl


class IOBTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        return [(token, token.ent_iob_) for token in args]
