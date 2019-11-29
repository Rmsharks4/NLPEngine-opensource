"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains implementation class to calculate the TP/FP/TN/FN counts of the provided predicted and actual labels.

Class Functions:
evaluate_metric
"""


import logging
from AIEvaluation.aievaluation.bl.EvaluationMetricsAbstractHandler import EvaluationMetricsAbstractHandler
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from sklearn.metrics import confusion_matrix


class ModelConfusionMatrixHandlerImpl(EvaluationMetricsAbstractHandler):
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def evaluate_metric(self, predicted_target, actual_target):
            """
            :param predicted_target: An array containing the predicted outcome of the model.
            :param actual_target: An array containing the actual outcome values.
            :return: A confusion matrix.

            """
            try:
                self.logger.info('Going to calculate the Confusion Matrix')
                confusion_matx = confusion_matrix(actual_target, predicted_target).ravel()
                return confusion_matx

            except Exception as exp:
                self.logger.error('Exception occured while getting the confusion matrix')
                raise CommonBaseException(exp)
