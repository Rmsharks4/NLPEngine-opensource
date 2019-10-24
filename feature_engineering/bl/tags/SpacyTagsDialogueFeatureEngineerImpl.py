from feature_engineering.bl.tags.AbstractTagsDialogueFeatureEngineerImpl import AbstractTagsDialogueFeatureEngineerImpl
import spacy
import neuralcoref


class SpacyTagsDialogueFeatureEngineerImpl(AbstractTagsDialogueFeatureEngineerImpl):

    def tags(self, args):
        nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(nlp)
        return nlp(args)
