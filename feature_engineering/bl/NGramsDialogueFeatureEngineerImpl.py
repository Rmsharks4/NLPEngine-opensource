from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from feature_engineering.bl.tags.TokenTagsDialogueFeatureEngineerImpl import TokenTagsDialogueFeatureEngineerImpl
from feature_engineering.utils.NGramLimit import NGramLimit


class NGramsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __init__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [[TokenTagsDialogueFeatureEngineerImpl.__name__]]
        self.config_pattern.properties.req_input = None
        self.config_pattern.properties.req_args = NGramLimit.__name__

    def engineer_feature_operation(self, args):

        # print(args.keys())

        for req_input in self.config_pattern.properties.req_input:
            for input in req_input:
                if input in args:
                    return args[input]\
                        .apply(lambda x: self.ngram(str(x), args[self.config_pattern.properties.req_args].ngram))

    def ngram(self, data, ngram_lim):
        return zip(*[data[i:] for i in range(ngram_lim)])
