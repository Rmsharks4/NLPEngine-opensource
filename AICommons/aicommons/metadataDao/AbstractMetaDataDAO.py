"""
Authors: sfatima@i2cinc.com.

Purpose:
This file contains an abstract class with the abstract function(s) that all meta data DAOs need to implement.

Abstract Functions:
__init__
load_meta_data

"""


import abc
import logging
from aicommonspython.utils.Constants import Constants


class AbstractMetaDataDAO(metaclass=abc.ABCMeta):
    """
    An abstract class to create different DAOs for different types of databases
    """

    _FETCH_INTERFACE_INSTANCES = """
        select instance_id 
        from interface_instances
        where interface_id = ? AND is_active = 'Y'
        """

    @abc.abstractmethod
    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    @abc.abstractmethod
    def load_meta_data(self,instance_id, query_dict):
        pass
