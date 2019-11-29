"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains handler class that executes evaluation for each metric provided. If metric list is empty then default
metric list is used to evaluate the predicted and actual labels.

Class Functions:
perform_model_evaluation
perform_metrics_evaluation
perform_evaluation_on_given_metric
"""

from AIEvaluation.aievaluation.bl.EvaluationMetricsAbstractFactory import EvaluationMetricsAbstractFactory
from AIEvaluation.aievaluation.utils.EvaluationUtils import EvaluationUtils
import logging
from AICommons.aicommons.commonutils.CommonUtilities import CommonUtilities
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIEvaluation.aievaluation.utils.Constants import Constants
from pandas import DataFrame




class ModelEvaluationHandler:
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def __validate_evaluation_metric_type(self, evaluation_metric_list, default_evaluations):
        invalid_metrics = set(evaluation_metric_list).difference(set(default_evaluations))
        if invalid_metrics:
            for invalid_metric in invalid_metrics:
                evaluation_metric_list.remove(invalid_metric)


    def perform_model_evaluation(self, evaluation_metric_list, predicted_target, actual_target):
        """
        :param evaluation_metric_list: List of metrics to be evaluated.
        :param predicted_target: An array containing the predicted outcome of the model.
        :param actual_target: An array containing the actual outcome values.
        :return: A Dataframe containing the evaluated metrics specified in the 'evaluation_metric_list'.
        """
        try:
            default_evaluations = EvaluationUtils.get_default_evaluation_metric_list()
            if not evaluation_metric_list:
                self.logger.warning('evaluation_metrics_list is empty, going to fetch default metrics list')
                evaluation_metric_list = default_evaluations

            self.logger.warning("Validating the 'evaluation_metric_list' values for admissible metric types")
            self.__validate_evaluation_metric_type(evaluation_metric_list, default_evaluations)

            metric_results_df = self.perform_metrics_evaluation(evaluation_metric_list, predicted_target, actual_target)
            self.logger.info('Metrics Evaluated successfully')
            return metric_results_df

        except CommonBaseException as exp:
            raise exp
        except DataFrameException as exp:
            raise CommonBaseException(exp)



    def perform_metrics_evaluation(self, evaluation_metric_list, predicted_target, actual_target):
        """
            :param evaluation_metric_list: List of metrics to be evaluated.
            :param predicted_target: An array containing the predicted outcome of the model.
            :param actual_target: An array containing the actual outcome values.
            :return: A Dataframe containing the evaluated metrics specified in the 'evaluation_metric_list'.
        """
        metrics_evaluation_dict = {}
        confusion_matrix_cache = None
        try:
                for metric_id in evaluation_metric_list:
                        self.logger.info('Performing evaluation for metricID = ' + str(metric_id))

                        self.logger.info('Saving evaluation score in metrics evaluation dictionary for metricID = ' + str(metric_id))
                        if metric_id in set(Constants.ConfusionMatrixTags):
                            if confusion_matrix_cache is None:
                                confusion_matrix_list = self.perform_evaluation_on_given_metric(metric_id,
                                                                                                predicted_target,
                                                                                                actual_target)
                                confusion_matrix_cache= {metric: score for metric, score in zip(Constants.ConfusionMatrixTags, confusion_matrix_list)}
                            metrics_evaluation_dict[metric_id]= [confusion_matrix_cache[metric_id]]
                        else:
                            metric_evaluation_score = self.perform_evaluation_on_given_metric(metric_id,
                                                                                              predicted_target,
                                                                                              actual_target)
                            metrics_evaluation_dict[metric_id] = [metric_evaluation_score]
                metric_results_df = DataFrame(metrics_evaluation_dict).T
                metric_results_df.columns=[""]
                return metric_results_df

        except DataFrameException as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            self.logger.error(
                'Exception occured while performing metrics evaluations')
            raise CommonBaseException(exp)


    def perform_evaluation_on_given_metric(self, metric_id, predicted_target, actual_target):
        """
        :param metric_id: Metric Id for which to evaluate
        :param predicted_target: An array containing the predicted outcome of the model.
        :param actual_target: An array containing the actual outcome values.
        :return evaluated_metric: A possible score for the metric type (A list of metrics falling under Confusion matrix' scope)

        """
        try:
            evaluation_handler = EvaluationMetricsAbstractFactory.get_evaluation_metric_handler_instance(metric_id)
            evaluated_metric = evaluation_handler.evaluate_metric(predicted_target, actual_target)
            return evaluated_metric

        except CommonBaseException as exp:
            raise exp
