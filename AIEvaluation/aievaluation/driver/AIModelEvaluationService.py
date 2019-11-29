"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains Driver class that will handle the incoming requests for metric evaluation of predicted and actual labels.

Class Functions:
evaluate_model
"""

import logging
from AIEvaluation.aievaluation.bl.ModelEvaluationHandler import ModelEvaluationHandler
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
import numpy as np


class AIModelEvaluationService:

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def __argument_type_validation(self, evaluation_metric_list, predicted_target, actual_target):
        if not isinstance(evaluation_metric_list, list):
            self.logger.error("InvalidInfoException : argument 'evaluation_metric_list' is not of type 'list'")
            raise InvalidInfoException("argument 'evaluation_metric_list' is not of type 'list'")
        if not isinstance(predicted_target, np.ndarray):
            self.logger.error("InvalidInfoException : argument 'predicted_target' is not of type 'np.ndarray'")
            raise InvalidInfoException("argument 'predicted_target' is not of type 'np.ndarray'")
        if not isinstance(actual_target, np.ndarray):
            self.logger.error("InvalidInfoException : argument 'actual_target' is not of type 'np.ndarray'")
            raise InvalidInfoException("argument 'actual_target' is not of type 'np.ndarray'")

    def __argument_none_validation(self, evaluation_metric_list, predicted_target, actual_target):
        if evaluation_metric_list is None:
            self.logger.error("MissingMandatoryFieldException : 'evaluation_metric_list' argument is None")
            raise MissingMandatoryFieldException("'evaluation_metric_list' argument is None")
        if predicted_target is None:
            self.logger.error("MissingMandatoryFieldException : 'predicted_target' argument is None")
            raise MissingMandatoryFieldException("'predicted_target' argument is None")
        if actual_target is None:
            self.logger.error("MissingMandatoryFieldException : 'actual_target' argument is None")
            raise MissingMandatoryFieldException("'actual_target' argument is None")


    def evaluate_model(self, evaluation_metric_list, predicted_target, actual_target):
        """
        :param evaluation_metric_list: A List of the metrics to be evaluated.
        :param predicted_target: A list containing the predicted outcome of the model.
        :param actual_target: A list containing the actual outcome values.
        :return: A Dataframe containing the evaluated metrics specified in the 'evaluation_metric_list'.
        """
        try:

            self.logger.warning("Validating the arguments")
            self.__argument_none_validation(evaluation_metric_list, predicted_target, actual_target)
            self.__argument_type_validation(evaluation_metric_list, predicted_target, actual_target)

            # :todo: Have to evaluate against model code

            self.logger.info('Going to perform Model evaluation')
            model_evaluation_handler = ModelEvaluationHandler()
            metric_results_df = model_evaluation_handler.perform_model_evaluation(evaluation_metric_list, predicted_target, actual_target)
            self.logger.warning('Model evaluation completed successfully')
            return metric_results_df

        except MissingMandatoryFieldException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            self.logger.error('Exception occured while evaluating model with evaluation metric list : ' + str(evaluation_metric_list))
            raise CommonBaseException(exp)

