"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains implementation class to evaluate F1-score of the provided predicted and actual labels

Class Functions:
evaluate_metric
"""

import logging
from AIEvaluation.aievaluation.bl.EvaluationMetricsAbstractHandler import EvaluationMetricsAbstractHandler
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
from sklearn.metrics import f1_score

class ModelF1EvaluationHandlerImpl(EvaluationMetricsAbstractHandler):
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def evaluate_metric(self, predicted_target, actual_target):
        """
        :param predicted_target: An array containing the predicted outcome of the model.
        :param actual_target: An array containing the actual outcome values.
        :return: F1-score.

        """
        try:
            self.logger.info('Going to calculate F1-score')
            return f1_score(actual_target, predicted_target)

        except Exception as exp:
            self.logger.error('Exception occured while calculating F-measure metric')
            raise CommonBaseException(exp)
