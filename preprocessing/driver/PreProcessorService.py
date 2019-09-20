import logging

from preprocessing.bl.AbstractDialoguePreProcessorFactory import AbstractDialoguePreProcessorFactory
from preprocessing.bl.AbstractDialoguePreProcessor import AbstractDialoguePreProcessor
from preprocessing.utils.PreProcessingLogger import PreProcessingLogger
from commons.dao.AbstractDAOFactory import AbstractDAOFactory
from commons.dao.SparkDAOImpl import SparkDAOImpl
from commons.dao.ConfigDAOImpl import ConfigDAOImpl
from commons.AbstractService import AbstractService
from preprocessing.bl.AbstractDialoguePreProcessorHandlerFactory import AbstractDialoguePreProcessorHandlerFactory
from preprocessing.bl.StandardFlowDialoguePreProcessorHandlerImpl import StandardFlowDialoguePreProcessorHandlerImpl


class PreProcessorService(AbstractService):

    def __init__(self):
        self.logger = logging.getLogger(PreProcessingLogger.__class__.__name__)

    def run(self, args):

        dao_obj = AbstractDAOFactory.get_dao(SparkDAOImpl.__class__.__name__)
        data_obj = dao_obj.load(args[SparkDAOImpl.__class__.__name__])

        handler_obj = AbstractDialoguePreProcessorHandlerFactory.get_dialogue_preprocessor_handler(StandardFlowDialoguePreProcessorHandlerImpl.__class__.__name__)
        output_obj = handler_obj.perform_preprocessing({
            AbstractDialoguePreProcessor.__class__.__name__: args[StandardFlowDialoguePreProcessorHandlerImpl.__class__.__name__],
            SparkDAOImpl.__class__.__name__: data_obj
        })

        return dao_obj.save(output_obj)
