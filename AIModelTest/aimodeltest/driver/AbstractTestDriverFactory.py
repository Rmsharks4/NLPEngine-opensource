"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an abstract Test driver factory class, it is meant to create and return the object of
prediction driver provided as parameter.

Class Functions:
get_instance


"""

import logging

from abc import ABC, abstractmethod


from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIModelTest.aimodeltest.utils.Constants import Constants
from AICommons.aicommons.dictionaryutils.DictionaryUtils import DictionaryUtils
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AIModelTest.aimodeltest.driver.ModelTestDriver import ModelTestDriver


class AbstractTestDriverFactory(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_instance(cls):
        """
        Authors: smunawar02@i2cinc.com
        Makes an object of the required Test driver and returns it
        :return: the object of corresponding test_driver
        """

        cls.logger.info("Getting test driver class")

        prediction_driver = ModelTestDriver()

        cls.logger.info("Returning Test driver class ")
        return prediction_driver

