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
    def get_instance(cls):
        """
        Authors: smunawar@i2cinc.com
        Makes an object of the required train driver and returns it

        :return: the object of corresponding train_driver
        """

        cls.logger.info("Getting train driver class ")

        train_driver = ModelTrainDriver()

        cls.logger.info("Returning train driver")
        return train_driver

