"""
Authors: afarooq01@i2cinc.com.

Purpose:
This file contains an abstract factory class, with a class function to get the desired database DAO

Class Functions:
get_machine_learning_model_dao

"""

import logging

from abc import ABC

from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.utils.Constants import Constants


class AbstractMachineLearningModelDAOFactory(ABC):
    """
    An abstract class to create different DAOs for different types of databases
    """

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_machine_learning_model_dao(cls, database_dialect):
        """

        :param database_dialect: name of database
        :return: concrete class object of required DAO
        """

        return