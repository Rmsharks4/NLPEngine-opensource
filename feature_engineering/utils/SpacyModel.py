import spacy
import neuralcoref
from feature_engineering.utils.AbstractUtils import AbstractUtils


class SpacyModel(AbstractUtils):

    nlp = None

    @staticmethod
    def load():
        SpacyModel.nlp = spacy.load('en_core_web_sm')
        neuralcoref.add_to_pipe(SpacyModel.nlp)
