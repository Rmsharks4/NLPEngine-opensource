"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains an Abstract Train Driver class, with functions generically applicable to all Train Drivers (
or overridden).

Class Functions:

train_model

"""

import logging


from abc import ABC, abstractmethod

from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from AIModelTrain.aimodeltrain.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants


class AbstractTrainDriver(ABC):

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @abstractmethod
    def train_model(self, data, target, model_params, model_hyper_params, model_cross_validator_params):
        pass
