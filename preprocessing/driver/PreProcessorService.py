"""
@Authors:
Ramsha Siddiqui - rsiddiqui@i2cinc.com

@Description:
this class contains a 'run' function that runs the whole routine - starting from DAO to BL to DAO again.
- An implementation of **Abstract Service** in NLP.commons
- Implements the following main function: **run**

"""

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
        self.logger = logging.getLogger(PreProcessingLogger.__name__)

    def run(self, args):

        dao_obj = AbstractDAOFactory.get_dao(SparkDAOImpl.__name__)
        data_obj = dao_obj.load(args[SparkDAOImpl.__name__])

        handler_obj = AbstractDialoguePreProcessorHandlerFactory.get_dialogue_preprocessor_handler(StandardFlowDialoguePreProcessorHandlerImpl.__name__)
        output_obj = handler_obj.perform_preprocessing({
            AbstractDialoguePreProcessor.__name__: args[StandardFlowDialoguePreProcessorHandlerImpl.__name__],
            SparkDAOImpl.__name__: data_obj
        })

        return dao_obj.save(output_obj)
