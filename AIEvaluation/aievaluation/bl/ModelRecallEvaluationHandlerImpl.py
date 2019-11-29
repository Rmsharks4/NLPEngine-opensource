"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains implementation class to evaluate Recall score of the provided predicted and actual labels

Class Functions:
evaluate_metric
"""

import logging
from AIEvaluation.aievaluation.bl.EvaluationMetricsAbstractHandler import EvaluationMetricsAbstractHandler
from AIEvaluation.aievaluation.utils.EvaluationUtils import EvaluationUtils
from CommonExceps.commonexceps.CommonInvalidArgumentException import CommonInvalidArgumentException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from sklearn.metrics import recall_score

class ModelRecallEvaluationHandlerImpl(EvaluationMetricsAbstractHandler):
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def evaluate_metric(self, predicted_target, actual_target):
        """
        :param predicted_target: An array containing the predicted outcome of the model.
        :param actual_target: An array containing the actual outcome values.
        :return: Recall score.
        """
        try:
            self.logger.info('Going to calculate recall score')
            return recall_score(actual_target, predicted_target)

        except Exception as exp:
            self.logger.error('Exception occured while calculating recall metric')
            raise CommonBaseException(exp)
