from vectorization.bl.AbstractVectorizerHandler import AbstractVectorizerHandler
from vectorization.bl.AbstractDialogueVectorizerFactory import AbstractDialogueVectorizerFactory
from vectorization.utils.VectorizationLogger import VectorizationLogger
import logging


class StandardFlowVectorizerHandlerImpl(AbstractVectorizerHandler):

    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(VectorizationLogger.__name__)

    def perform_vectorization(self, args):
        """

        :param args: gets data in arguments and then passes it according to the number and types of configurations
        """
        # TODO: add handler code here!
        pass
