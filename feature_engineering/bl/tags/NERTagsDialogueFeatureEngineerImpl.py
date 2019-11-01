from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl


class NERTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        return [(token, token.ent_type_) for token in args if token.ent_type_ != '']
