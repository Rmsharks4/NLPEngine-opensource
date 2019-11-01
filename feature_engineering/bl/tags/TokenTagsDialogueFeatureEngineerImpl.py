from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl


class TokenTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        return [token for token in args]
