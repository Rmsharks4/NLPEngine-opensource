from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.utils.VectorizationConstants import VectorizationConstants
from vectorization.bl.OneHotDataStructureImpl import OneHotDataStructureImpl


class OneHotDialogueVectorizer(AbstractDialogueVectorizer):

    def __init__(self):
        super().__init__()
        self.data_structure = OneHotDataStructureImpl()

    def vectorize_operation(self, args):
        """

        :param args: SHOULD CONTAIN: A CHARACTER/WORD/SENTENCE/DOCUMENT TO VECTORIZE
        """
        if args not in self.data_structure.dictionary.keys():
            self.data_structure.dictionary[args] = max(self.data_structure.integer_encoder.items()) + VectorizationConstants.SINGULAR_INCREMENT
        self.data_structure.sparse_encoder.append(args)
        self.data_structure.integer_encoder.append(self.data_structure.dictionary[args])
        self.data_structure.binary_encoder.append([int(x) for x in bin(self.data_structure.dictionary[args])[2:]])

    def aggregate(self):
        pass
