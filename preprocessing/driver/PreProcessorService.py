import logging

from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from commons.dao.AbstractDAOFactory import AbstractDAOFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl
from commons.dao.ConfigDAOImpl import ConfigDAOImpl
from commons.AbstractService import AbstractService


class PreProcessorService(AbstractService):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingLogger.__class__.__name__)

    def run(self, args):
        # the order should be given as:
        # 1. read dao
        # 2. pre-process
        # 3. write dao
        dao_obj = AbstractDAOFactory.get_dao(SparkDAOImpl.__class__.__name__)
        dao_obj.load(args[self.__class__.__name__])

        pass
