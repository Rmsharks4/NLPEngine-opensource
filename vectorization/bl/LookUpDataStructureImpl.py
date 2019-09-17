from vectorization.bl.AbstractDataStructure import AbstractDataStructure


class LookUpDataStructureImpl(AbstractDataStructure):

    def __init__(self):
        super().__init__()
        self.counts = dict()
        self.dictionary = dict()
