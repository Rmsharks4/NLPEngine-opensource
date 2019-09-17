
from pyspark.sql import SQLContext
from pyspark.sql import DataFrameReader
from pyspark.sql import DataFrame

from preprocessing.dao.AbstractPreProcessorDAO import AbstractPreProcessorDAO
from preprocessing.utils.PreProcessingConstants import PreProcessingConstants


class StandardPreProcessorDAOImpl(AbstractPreProcessorDAO):

    def __init__(self):
        super().__init__()

    @classmethod
    def __check_common_input_params(cls, args):
        pass

    @classmethod
    def __check_load_data_input_params(cls, args):
        pass

    @classmethod
    def __check_save_data_input_params(cls, args):
        pass

    @classmethod
    def load_data(cls, args):
        pass

    @classmethod
    def save_data(cls, args):
        pass
