"""
Authors: smunawar02@i2cinc.com

Purpose:


Class Functions:
get_evaluation_metric_handler_instance
"""



import abc
from AIEvaluation.aievaluation.bl.ModelF1EvaluationHandlerImpl import ModelF1EvaluationHandlerImpl
from AIEvaluation.aievaluation.bl.ModelPrecisionEvaluationHandlerImpl import ModelPrecisionEvaluationHandlerImpl
from AIEvaluation.aievaluation.bl.ModelRecallEvaluationHandlerImpl import ModelRecallEvaluationHandlerImpl
from AIEvaluation.aievaluation.bl.ModelAccuracyEvaluationHandlerImpl import ModelAccuracyEvaluationHandlerImpl
from AIEvaluation.aievaluation.bl.ModelConfusionMatrixHandlerImpl import ModelConfusionMatrixHandlerImpl
from AIEvaluation.aievaluation.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants

class EvaluationMetricsAbstractFactory(metaclass=abc.ABCMeta):
    @classmethod
    def get_evaluation_metric_handler_instance(cls, metric_id):
        """
        :param metric_id: Metric Id on which to evaluate predicted and actual labels.
               Metric Id(s) defined in constants.py
        :return: An implementation for the requested metric type
        """

        if metric_id == CommonConstants.PRECISION_METRIC_ID:
            return ModelPrecisionEvaluationHandlerImpl()
        if metric_id == CommonConstants.RECALL_METRIC_ID:
            return ModelRecallEvaluationHandlerImpl()
        if metric_id == CommonConstants.FMEASURE_METRIC_ID:
            return ModelF1EvaluationHandlerImpl()
        if metric_id == CommonConstants.ACCURACY_METRIC_ID:
            return ModelAccuracyEvaluationHandlerImpl()
        if metric_id in Constants.ConfusionMatrixTags:
            return ModelConfusionMatrixHandlerImpl()

