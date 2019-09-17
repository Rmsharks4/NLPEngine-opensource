from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.utils.MathematicsUtils import MathematicsUtils
from vectorization.bl.TFIDFDataStructureImpl import TFIDFDataStructureImpl
from vectorization.utils.VectorizationConstants import VectorizationConstants


class TFIDFDialogueVectorizer(AbstractDialogueVectorizer):

    def __init__(self):
        """

        :param args:
        """
        super().__init__()
        self.data_structure = TFIDFDataStructureImpl()

    def vectorize_operation(self, args):
        """
        :param args: SHOULD CONTAIN: A CHARACTER/WORD/SENTENCE/DOCUMENT TO VECTORIZE
        """
        if args in self.data_structure.counts.keys():
            self.data_structure.counts[args] = VectorizationConstants.SINGULAR_INCREMENT
        else:
            self.data_structure.counts[args] += VectorizationConstants.SINGULAR_INCREMENT
        self.data_structure.sparse_encoder.append(args)
        self.data_structure.length += VectorizationConstants.SINGULAR_INCREMENT

    def aggregate(self):
        for key in self.data_structure.sparse_encoder:
            self.data_structure.tfidf_encoder.append(
                MathematicsUtils.divide([
                    self.data_structure.counts[key], self.data_structure.length
                ])
            )
