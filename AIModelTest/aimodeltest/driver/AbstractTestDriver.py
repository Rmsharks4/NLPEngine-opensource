"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an Abstract Test Driver class, with functions generically applicable to all Test Drivers (
or overridden).

Class Functions:

test_model

"""
import logging


from abc import ABC, abstractmethod

from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIModelTest.aimodeltest.utils.Constants import Constants
from AICommons.aicommons.dictionaryutils.DictionaryUtils import DictionaryUtils
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants


class AbstractTestDriver(ABC):
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @abstractmethod
    def test_model(self, test_data, model_params, trained_model):
        pass