from feature_engineering.bl.chunks.AbstractChunksDialogueFeatureEngineerImpl import AbstractChunksDialogueFeatureEngineerImpl
import nltk


class NLTKNERChunksDialogueFeatureEngineerImpl(AbstractChunksDialogueFeatureEngineerImpl):

    def chunks(self, args):
        return nltk.ne_chunk(args)
