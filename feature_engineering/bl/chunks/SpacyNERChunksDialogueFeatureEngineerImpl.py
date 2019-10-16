from feature_engineering.bl.chunks.AbstractChunksDialogueFeatureEngineerImpl import AbstractChunksDialogueFeatureEngineerImpl
import spacy


class NLTKNERChunksDialogueFeatureEngineerImpl(AbstractChunksDialogueFeatureEngineerImpl):

    def chunks(self, args):
        nlp = spacy.load('en_core_web_sm')
        return [(X, X.ent_iob_, X.ent_type_) for X in nlp(args)]
