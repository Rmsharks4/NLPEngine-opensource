"""
Authors: sfatima@i2cinc.com.

Purpose:
This file contains a concrete class which defines the operations to read and write data to/from informix database

Class Functions:
__db_conn_validation
__dict_validaton
load_meta_data

"""

import logging
import ibm_db

from aicommonspython.metadataDao.AbstractMetaDataDAO import AbstractMetaDataDAO
from aicommonspython.sparkProperties.SparkProperties import SparkProperties
from commonexceps.SQLException import SQLException

from aicommonspython.utils.Constants import Constants
from aicommonspython.commonutils.CommonConstants import CommonConstants

from commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from commonexceps.InvalidInfoException import InvalidInfoException
from commonexceps.CommonBaseException import CommonBaseException
from databasehandler.DatabaseHandler import DatabaseHandler


class InformixMetaDataDAOImpl(AbstractMetaDataDAO):
    """
    A concrete class to implement database operations for Postgres database
    """

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def __db_conn_validation(self, informix_multi_instance_spark_prop, informix_single_instance_spark_prop):
        if informix_multi_instance_spark_prop is not None:
            if not isinstance(informix_multi_instance_spark_prop, SparkProperties):
                self.logger.error('InvalidInfoException : argument informix_multi_instance_spark_prop is not of type SparkProperties')
                raise InvalidInfoException('argument informix_multi_instance_spark_prop is not of type SparkProperties')
        if informix_single_instance_spark_prop is not None:
            if not isinstance(informix_single_instance_spark_prop, SparkProperties):
                self.logger.error('InvalidInfoException : argument informix_single_instance_spark_prop is not of type SparkProperties')
                raise InvalidInfoException('argument informix_single_instance_spark_prop is not of type SparkProperties')

    def __dict_validaton(self, query_dict):
        if query_dict is None:
            self.logger.error('MissingMandatoryFieldException : query_dict argument is None')
            raise MissingMandatoryFieldException('query_dict argument is None')
        if not isinstance(query_dict, dict):
            self.logger.error('InvalidInfoException : argument query_dict is not of type dict')
            raise InvalidInfoException('argument query_dict is not of type dict')
        for key, value in query_dict.items():
            if value is None:
                self.logger.error('MissingMandatoryFieldException : value: ' + str(value) + ' in query_dict.items is None')
                raise MissingMandatoryFieldException('value: ' + str(value) + ' in query_dict.items is None')
            if not isinstance(value, dict):
                self.logger.error('InvalidInfoException :  value: ' + str(value) + ' in query_dict.items is not of type dict')
                raise InvalidInfoException('value: ' + str(value) + ' in query_dict.items is not of type dict')
            for innner_key, inner_value in value.items():
                if inner_value is None:
                    self.logger.error('MissingMandatoryFieldException : inner_value: ' + str(inner_value) + ' in value.items() is None')
                    raise MissingMandatoryFieldException('inner_value: ' + str(inner_value) + ' in value.items() is None')
                if not isinstance(inner_value, str):
                    self.logger.error('InvalidInfoException : inner_value: ' + str(inner_value) + ' in value.items() is not of type str')
                    raise InvalidInfoException('inner_value: ' + str(inner_value) + ' in value.items() is not of type str')

    def __load_meta_data_argument_validation(self, informix_multi_instance_spark_prop,informix_single_instance_spark_prop, query_dict):
        try:
            self.logger.info('Function: __load_meta_data_argument_validation, Class: InformixMetaDataDAOImpl')
            self.__db_conn_validation(informix_multi_instance_spark_prop=informix_multi_instance_spark_prop, informix_single_instance_spark_prop = informix_single_instance_spark_prop)
            self.__dict_validaton(query_dict=query_dict)
        except MissingMandatoryFieldException as exp:
            raise CommonBaseException(exp)
        except InvalidInfoException as exp:
            raise CommonBaseException(exp)

    def load_meta_data(self, instance_id, query_dict):
        """
        :param query_dict: unique identifier for the model
        :param instance_id: an instance_id to use for data retrieval
        :return: dictionary of tables read
        """

        metadata_dict = {}
        # conn_informix_multi_inst = None
        try:

            self.logger.warning("Going to get connection for :" + instance_id)
            instance_conn = DatabaseHandler.get_connection(instance_id)

            # cursor = instance_conn.cursor()

            self.logger.warning("Going to load metadata.")
            for mapping_name, query_schema_dictionary in query_dict.items():
                self.logger.warning("Going to load metadata for query: " + str(query_schema_dictionary[CommonConstants.QUERY_TAG]))
                cursor = instance_conn.cursor()
                cursor.execute(query_schema_dictionary[CommonConstants.QUERY_TAG])
                temp_dict_for_table = {}
                records = cursor.fetchall()
                for row in records:
                    key = row[0]
                    value = row[1]
                    temp_dict_for_table[key] = value
                metadata_dict[mapping_name] = temp_dict_for_table
                if (cursor is not None) & (not cursor._closed):
                    DatabaseHandler.logger.debug('Closing cursor...')
                    cursor.close()

        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            self.logger.error("SQLException : Meta Data Dictionary could not be loaded")
            raise SQLException(exp)

        finally:
            self.logger.warning("Closing Connection")
            DatabaseHandler.commit_and_close_resources(instance_conn, cursor)

        return metadata_dict

    def load_interface_instances(self, interface_id, mi_instance_id):
        """
        :param interface_id: AI Fraud interface id
        :param mi_instance_id: multi instance id for Db conn
        :return: list of instances read
        """
        interface_instances = []
        try:
            self.logger.warning("Going to load instances for interface_id: " + str(interface_id))

            db_multi_instance_conn = DatabaseHandler.get_connection(str(mi_instance_id))

            cursor = db_multi_instance_conn.cursor()
            record_tuple = (interface_id,)
            cursor.execute(AbstractMetaDataDAO._FETCH_INTERFACE_INSTANCES, record_tuple)

            records = cursor.fetchall()
            for row in records:
                instance_id = row[0]
                interface_instances.append(instance_id)

        except Exception as exp:
            self.logger.error("Instances could not be retrieved against interface id: " + str(interface_id))
            raise SQLException("Instances could not be retrieved against interface id: " + str(interface_id), exp)

        finally:
            self.logger.warning("closing connection")
            DatabaseHandler.commit_and_close_resources(db_multi_instance_conn, cursor)

        return interface_instances
