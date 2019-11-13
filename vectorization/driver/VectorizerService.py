import pandas as pd
import logging
from commons.config.AbstractConfig import AbstractConfig
from vectorization.utils.VectorizationLogger import VectorizationLogger
from commons.dao.PandasDAOImpl import PandasDAOImpl
from vectorization.bl.AbstractDialogueVectorizer import AbstractDialogueVectorizer
from vectorization.bl.AbstractVectorizerHandlerFactory import AbstractVectorizerHandlerFactory
from vectorization.bl.StandardFlowVectorizerHandlerImpl import StandardFlowVectorizerHandlerImpl
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException


class VectorizerService:

    def __init__(self):
        """
        initializes Pre-processor service class and starts logger.
        """
        self.logger = logging.getLogger(VectorizationLogger.__name__)

    def run(self, args):
        handler_obj = AbstractVectorizerHandlerFactory.get_vectorizer_handler(StandardFlowVectorizerHandlerImpl.__name__)
        return handler_obj.perform_preprocessing({
            AbstractDialogueVectorizer.__name__: args[StandardFlowVectorizerHandlerImpl.__name__],
            PandasDAOImpl.__name__: args[PandasDAOImpl.__name__]
        })
        pass

    def validation(self, args):
        if args is None:
            self.logger.error(MissingMandatoryFieldException.__name__, 'Given:', type(None))
            raise MissingMandatoryFieldException('Given:', type(None))
        if not isinstance(args, dict):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args), 'Required:', type(dict))
            raise InvalidInfoException('Given:', type(args), 'Required:', type(dict))
        if StandardFlowVectorizerHandlerImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(), 'Required:', StandardFlowVectorizerHandlerImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(),
                                                 'Required:', StandardFlowVectorizerHandlerImpl.__name__)
        if args[StandardFlowVectorizerHandlerImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(list))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(list))
        if not isinstance(args[StandardFlowVectorizerHandlerImpl.__name__], list):
            self.logger.error(InvalidInfoException.__name__,
                              'Given:', type(args[StandardFlowVectorizerHandlerImpl.__name__]),
                              'Required:', type(list))
            raise InvalidInfoException('Given:', type(args[StandardFlowVectorizerHandlerImpl.__name__]),
                                       'Required:', type(list))
        for config in args[StandardFlowVectorizerHandlerImpl.__name__]:
            if not isinstance(config, AbstractConfig):
                self.logger.error(InvalidInfoException.__name__,
                                  'Given:', type(config), 'Required:', type(AbstractConfig))
                raise InvalidInfoException('Given:', type(config), 'Required:', type(AbstractConfig))
        if PandasDAOImpl.__name__ not in args:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
            raise MissingMandatoryFieldException('Given:', args.items(), 'Required:', PandasDAOImpl.__name__)
        if args[PandasDAOImpl.__name__] is None:
            self.logger.error(MissingMandatoryFieldException.__name__,
                              'Given:', type(None), 'Required:', type(pd.DataFrame))
            raise MissingMandatoryFieldException('Given:', type(None), 'Required:', type(pd.DataFrame))
        return True
