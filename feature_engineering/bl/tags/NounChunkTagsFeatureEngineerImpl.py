from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl


class NounChunkTagsFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[AbstractTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = None

    def tags(self, args):
        return [chunk for chunk in args.noun_chunks]
