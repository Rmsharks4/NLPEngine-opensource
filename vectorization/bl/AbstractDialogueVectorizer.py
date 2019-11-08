from vectorization.utils.VectorizationConstants import VectorizationConstants
import logging
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl
import abc


class AbstractDialogueVectorizer(StandardConfigParserImpl):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(VectorizationConstants.LOGGER_NAME)
        self.cls_data_structure = None

    @property
    def data_structure(self):
        return self.cls_data_structure

    @data_structure.setter
    def data_structure(self, args):
        self.cls_data_structure = args

    @classmethod
    def vectorize(cls, args):
        if cls.vectorize_validation(args):
            cls.vectorize_operation(args)

    @classmethod
    def vectorize_validation(cls, args):
        return args

    def vectorize_operation(self, args):
        pass

    def aggregate(self):
        pass
