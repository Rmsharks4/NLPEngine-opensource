"""
Authors: smunawar02@i2c.com

Purpose: 
This file contains an abstract class with the abstract function(s) that all metric evaluation classes needs to implement

Functions:
evaluate_metric
"""

import abc


class EvaluationMetricsAbstractHandler(metaclass=abc.ABCMeta):
    """
    An abstract class with abstract methods for different metric evaluations
    """

    @abc.abstractmethod
    def evaluate_metric(self, predicted_target, actual_target):
        pass


