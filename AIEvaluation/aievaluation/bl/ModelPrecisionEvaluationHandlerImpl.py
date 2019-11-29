"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains implementation class to evaluate Precision score of provided predicted and actual labels

Class Functions:
evaluateMetric
"""
import logging
from AIEvaluation.aievaluation.bl.EvaluationMetricsAbstractHandler import EvaluationMetricsAbstractHandler
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from sklearn.metrics import precision_score


class ModelPrecisionEvaluationHandlerImpl(EvaluationMetricsAbstractHandler):
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def evaluate_metric(self, predicted_target, actual_target):
        """
        :param predicted_target: An array containing the predicted outcome of the model.
        :param actual_target: An array containing the actual outcome values.
        :return: Precision score.
        """
        try:
            self.logger.info('Going to calculate precision score')
            return precision_score(actual_target, predicted_target)

        except Exception as exp:
            self.logger.error('Exception occured while calculating precision metric')
            raise CommonBaseException(exp)

