from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
import spacy
import neuralcoref


class CoreferenceTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(nlp)
        doc = nlp(args)
        if doc._.has_coref:
            return doc._.coref_clusters
        return None

