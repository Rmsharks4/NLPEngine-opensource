from vectorization.bl.AbstractDataStructure import AbstractDataStructure


class OneHotDataStructureImpl(AbstractDataStructure):

    def __init__(self):
        super().__init__()
        self.dictionary = dict()
        self.sparse_encoder = []
        self.integer_encoder = []
        self.binary_encoder = []
