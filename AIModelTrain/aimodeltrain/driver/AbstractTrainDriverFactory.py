"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an abstract train driver class, it is meant to create and return the object of
train driver provided as a parameter.

Class Functions:
get_instance


"""

import logging

from abc import ABC


from AIModelTrain.aimodeltrain.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AIModelTrain.aimodeltrain.driver.ModelTrainDriver import ModelTrainDriver


class AbstractTrainDriverFactory(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_instance(cls, model_name):
        """
        Authors: smunawar@i2cinc.com
        Makes an object of the required train driver and returns it

        :param model_name: the name of required train driver ('random_forest','naive bayes' etc)
        :return: the object of corresponding train_driver
        """

        cls.logger.info("Getting driver class implementation for: " + str(model_name))
        train_driver = ""
        if model_name == CommonConstants.NAIVE_BAYES_TAG:
            train_driver = ModelTrainDriver()
        else:
            cls.logger.info("Invalid model_name")
            cls.logger.info("No train driver class implementation for: " + str(model_name))

        cls.logger.info("Returning train driver class implementation for: " + str(model_name))
        return train_driver

