from vectorization.bl.AbstractDataStructure import AbstractDataStructure
from gensim.models import Word2Vec


class EmbeddingDataStructureImpl(AbstractDataStructure):

    def __init__(self):
        super().__init__()
        self.corpus = []
        self.model = None

