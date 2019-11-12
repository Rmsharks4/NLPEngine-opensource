from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.bl.embedding.EmbeddingDataStructureImpl import EmbeddingDataStructureImpl
from gensim.models import Word2Vec


class EmbeddingDialogueVectorizer(AbstractDialogueVectorizer):

    def __init__(self):
        super().__init__()
        self.data_structure = EmbeddingDataStructureImpl()

    def vectorize_operation(self, args):
        """

        :param args: SHOULD CONTAIN: A CHARACTER/WORD/SENTENCE/DOCUMENT TO VECTORIZE
        """
        self.data_structure.corpus.append([word for word in args])

    def aggregate(self):
        self.data_structure.model = Word2Vec(
            self.data_structure.corpus,
            min_count=1,
            size=200,
            workers=2,
            window=5,
            iter=30
        )
