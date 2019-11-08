from vectorization.bl.AbstractDataStructure import AbstractDataStructure


class TFIDFDataStructureImpl(AbstractDataStructure):

    def __init__(self):
        super().__init__()
        self.length = 0
        self.counts = dict()
        self.dictionary = dict()
        self.sparse_encoder = []
        self.tfidf_encoder = []
