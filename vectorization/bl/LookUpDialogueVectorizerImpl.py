from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.utils.VectorizationConstants import VectorizationConstants
from vectorization.bl.LookUpDataStructureImpl import LookUpDataStructureImpl


class LookUpDialogueVectorizer(AbstractDialogueVectorizer):

    def __init__(self):
        super().__init__()
        self.data_structure = LookUpDataStructureImpl()

    def vectorize_operation(self, args):
        """

        :param args: SHOULD CONTAIN: A CHARACTER/WORD/SENTENCE/DOCUMENT TO VECTORIZE
        """
        if args not in self.data_structure.counts.keys():
            self.data_structure.counts[args] = VectorizationConstants.SINGULAR_INCREMENT
        else:
            self.data_structure.counts[args] += VectorizationConstants.SINGULAR_INCREMENT

    def aggregate(self):
        """
            Aggregate will inverse the counts of the dictionary and then create a new one -
            which will have the most occuring elements with the smallest index and vice versa!
        """
        idx = 0
        for (key, value) in sorted(self.data_structure.counts.items(), reverse=True):
            if value > VectorizationConstants.LOOKUP_THRESHOLD:
                self.data_structure.dictionary[key] = idx
                idx += 1
            else:
                break
