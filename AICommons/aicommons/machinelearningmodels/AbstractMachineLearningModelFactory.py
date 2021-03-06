"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an abstract machine learning model factory class, it is meant to create and return the object of
model name provided as parameter.

Class Functions:
get_instance

"""

import logging
from abc import ABC

from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.machinelearningmodels.NaiveBayesMachineLearningModelImpl import \
    NaiveBayesMachineLearningModelImpl
from AICommons.aicommons.utils.Constants import Constants
from deep_learning.bl.models.TFDeepLearningModelImpl import TFDeepLearningModelImpl


class AbstractMachineLearningModelFactory(ABC):

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_instance(cls, model_name):
        """
        Authors: smunawar02@i2cinc.com
        Makes an object of the required model and returns it

        :param model_name: the name of required model ('decision_tree', 'random_forest' etc)
        :return: An instance of the corresponding model
        """

        cls.logger.info("Getting model class implementation for: " + str(model_name))
        model = ""
        is_implemented = True

        if model_name == CommonConstants.NAIVE_BAYES_TAG:
            model = NaiveBayesMachineLearningModelImpl()
        elif model_name == TFDeepLearningModelImpl.__name__:
            model = TFDeepLearningModelImpl()
        else:
            cls.logger.info("Invalid model name")
            cls.logger.info("No model class implementation for: " + str(model_name))
            is_implemented = False

        if is_implemented:
            cls.logger.info("Returning model class implementation for: " + str(model_name))


        return model
