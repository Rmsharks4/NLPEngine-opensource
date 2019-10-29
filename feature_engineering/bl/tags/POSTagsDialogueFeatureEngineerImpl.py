from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl


class POSTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        return [(token, token.tag_) for token in args]
