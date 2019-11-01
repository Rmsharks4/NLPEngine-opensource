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
        return args[TokenTagsDialogueFeatureEngineerImpl.__name__].apply(
            lambda x: self.ngram(x, args[self.config_pattern.properties.req_args].ngram))

    def ngram(self, data, ngram_lim):
        ngrams = zip(*[data[i:] for i in range(ngram_lim)])
        return [''.join(str(ngram)) for ngram in ngrams]
