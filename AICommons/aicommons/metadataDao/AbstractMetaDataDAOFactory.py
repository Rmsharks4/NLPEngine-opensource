"""
Authors: sfatima@i2cinc.com.

Purpose:
This file contains an abstract factory class, with a class function to get the desired database DAO

Class Functions:
get_meta_data_dao

"""

import abc
import logging

from aicommonspython.commonutils.CommonConstants import CommonConstants

from aicommonspython.metadataDao.InformixMetaDataDAOImpl import InformixMetaDataDAOImpl
from aicommonspython.utils.Constants import Constants

from commonexceps.InvalidInfoException import InvalidInfoException


class AbstractMetaDataDAOFactory(metaclass=abc.ABCMeta):
    """
    An abstract class to create different DAOs for different types of databases
    """
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_meta_data_dao(cls, database_dialect):
        """

        :param database_dialect: (string) name of database
        :return: concrete class object of required DAO
        """
        cls.logger.info('Function: get_meta_data_dao, Class: AbstractMetaDataDAOFactory')

        if database_dialect == CommonConstants.DATABASE_INFORMIX:
            cls.logger.warning("Returning instance of " + CommonConstants.DATABASE_INFORMIX)
            return InformixMetaDataDAOImpl()

        elif database_dialect == CommonConstants.DATABASE_POSTGRES:
            pass

        elif database_dialect == CommonConstants.DATABASE_CASSANDRA:
            pass

        else:
            cls.logger.error('InvalidInfoException : Invalid database_dialect: No such database_dialect of preprocessing dao, given database_dialect was' + database_dialect)
            raise InvalidInfoException('Invalid database_dialect: No such database_dialect of preprocessing dao, given database_dialect was' + database_dialect)

