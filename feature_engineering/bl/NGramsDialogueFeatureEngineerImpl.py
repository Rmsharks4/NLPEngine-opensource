from feature_engineering.bl.AbstractDialogueFeatureEngineer import AbstractDialogueFeatureEngineer
from preprocessing.bl.SpellCheckerDialoguePreProcessorImpl import SpellCheckerDialoguePreProcessorImpl
from preprocessing.bl.WordNetLemmatizerDialoguePreProcessorImpl import WordNetLemmatizerDialoguePreProcessorImpl
from feature_engineering.utils.NGramLimit import NGramLimit


class NGramsDialogueFeatureEngineerImpl(AbstractDialogueFeatureEngineer):

    def __int__(self):
        super().__init__()
        self.config_pattern.properties.req_data = [SpellCheckerDialoguePreProcessorImpl.__name__,
                                                   WordNetLemmatizerDialoguePreProcessorImpl.__name__]
        self.config_pattern.properties.req_args = NGramLimit.__name__

    def engineer_feature_operation(self, args):
        for req_data in self.config_pattern.properties.req_data:
            if req_data in args:
                return self.ngram(args[req_data], args[self.config_pattern.properties.req_args].ngram)
        return None

    def ngram(self, data, ngram_lim):
        return zip(*[data[i:] for i in range(ngram_lim)])
