"""
Authors: hrafiq@i2cinc.com

Purpose:
This file contains an abstract train driver class, it is meant to create and return the object of
train driver provided as parameter.

Class Functions:
get_instance


"""

import logging

from abc import ABC, abstractmethod


from commonexceps.CommonBaseException import CommonBaseException
from aimodeltrain.utils.Constants import Constants
from aicommonspython.dictionaryutils.DictionaryUtils import DictionaryUtils
from aicommonspython.commonutils.CommonConstants import CommonConstants
from aimodeltrain.driver.ModelTrainDriver import ModelTrainDriver
from aimodeltrain.driver.AnomalyDetectionTrainDriver import AnomalyDetectionTrainDriver


class AbstractTrainDriverFactory(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_instance(cls, model_name):
        """
        Authors: hrafiq@i2cinc.com
        Makes an object of the required train driver and returns it

        :param model_name: the name of required train driver technique ('random_forest','HBOS' etc)
        :return: the object of corresponding train_driver
        """

        cls.logger.info("Getting driver class implementation for: " + str(model_name))
        train_driver = ""
        if model_name == CommonConstants.DECISION_TREE_TAG:
            train_driver = ModelTrainDriver()
        elif model_name == CommonConstants.RANDOM_FOREST_TAG:
            train_driver = ModelTrainDriver()
        elif model_name == CommonConstants.GRADIENT_BOOSTED_TREE_TAG:
            train_driver = ModelTrainDriver()
        elif model_name == CommonConstants.LOGISTIC_REGRESSION_TAG:
            train_driver = ModelTrainDriver()
        elif model_name == CommonConstants.NAIVE_BAYES_TAG:
            train_driver = ModelTrainDriver()
        elif model_name == CommonConstants.HBOS_TAG:
            train_driver = AnomalyDetectionTrainDriver()
        elif model_name == CommonConstants.MULTI_LAYER_PERCEPTRON_TAG:
            train_driver = ModelTrainDriver()
        else:
            cls.logger.info("Invalid model_name")
            cls.logger.info("No train driver class implementation for: " + str(model_name))

        cls.logger.info("Returning train driver class implementation for: "+ str(model_name))
        return train_driver

