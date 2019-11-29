"""
Authors: uahmad

Purpose:
This file contains Utility class that provides utility functionality of other classes.

Class Functions:
getDefaultEvaluationMetricList
getTruePositiveCount
getFalseNegativeCount
getTrueNegativeCount
getFalsePositiveCount
"""
import logging
from AIEvaluation.aievaluation.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from CommonExceps.commonexceps.CommonInvalidArgumentException import CommonInvalidArgumentException
from CommonExceps.commonexceps.DataFrameException import DataFrameException

class EvaluationUtils:
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @staticmethod
    def get_default_evaluation_metric_list():
        """
        :return: Default metric id(s) list
        """
        default_metric_list = [CommonConstants.PRECISION_METRIC_ID, CommonConstants.RECALL_METRIC_ID, CommonConstants.FMEASURE_METRIC_ID,CommonConstants.TRUE_POSITIVE_METRIC_ID,
                               CommonConstants.FALSE_POSITIVE_METRIC_ID,CommonConstants.TRUE_NEGATIVE_METRIC_ID,CommonConstants.FALSE_NEGATIVE_METRIC_ID,CommonConstants.ACCURACY_METRIC_ID]
        return default_metric_list





