import logging
import yaml
import logging.config

from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from pyspark.sql.types import StructType, StructField
from CommonExceps.commonexceps.InitializationException import InitializationException
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from AICommons.aicommons.utils.Constants import Constants
# from pywebhdfs.webhdfs import PyWebHdfsClient
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
import re

# TODO: Need to add docstrings


class CommonUtilities:

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def get_logger_level(cls, level_name):
        if CommonConstants.LOG_LEVEL_INFO == level_name:
            return logging.INFO
        elif CommonConstants.LOG_LEVEL_WARN == level_name:
            return logging.WARN
        elif CommonConstants.LOG_LEVEL_ERROR == level_name:
            return logging.ERROR
        else:
            return logging.DEBUG

    @classmethod
    def load_configurations(cls, config_file_path):
        try:
            with open(config_file_path, 'r') as ymlfile:
                config = yaml.load(ymlfile)
            return config
        except Exception as exp:
            cls.logger.error('Exception occured while loading configuration file ' + str(config_file_path))
            raise InitializationException("Exception occurred while loading configuration", exp)

    @classmethod
    def initialize_logger(cls, log_properties_file_path, train_test_prediction_mode):
        try:
            # with open('D://AI Repository//Trunk//Source//log4jTesting//resources//logConfig.yml', 'rt') as file:
            with open(log_properties_file_path, 'rt') as file:
                config = yaml.safe_load(file.read())
                if train_test_prediction_mode == '3' or train_test_prediction_mode is None:
                    config[CommonConstants.HANDLER_TAG][CommonConstants.FRAUD_ENGINE_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.FRAUD_ENGINE_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.COMMONS_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.COMMONS_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.PREPROCESSING_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.PREPROCESSING_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.MODEL_TRAIN_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.MODEL_TRAIN_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.PREDICTION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.PREDICTION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.FEATURE_ENGINEERING_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.FEATURE_ENGINEERING_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.TRANSFORMATION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.TRANSFORMATION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.EVALUATION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.EVALUATION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.HSM_GATEWAY_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.HSM_GATEWAY_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.MI_POOL_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.MI_POOL_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.DATABASE_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.DATABASE_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.PREDICTION_LOG_FOLDER_TAG)

                else:
                    config[CommonConstants.HANDLER_TAG][CommonConstants.FRAUD_ENGINE_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.FRAUD_ENGINE_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.COMMONS_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.COMMONS_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.PREPROCESSING_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.PREPROCESSING_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.MODEL_TRAIN_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.MODEL_TRAIN_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.PREDICTION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.PREDICTION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.FEATURE_ENGINEERING_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.FEATURE_ENGINEERING_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.TRANSFORMATION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.TRANSFORMATION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.EVALUATION_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.EVALUATION_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.HSM_GATEWAY_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.HSM_GATEWAY_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.MI_POOL_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.MI_POOL_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)
                    config[CommonConstants.HANDLER_TAG][CommonConstants.DATABASE_HANDLER_TAG][CommonConstants.FILENAME_TAG] = config[CommonConstants.HANDLER_TAG][CommonConstants.DATABASE_HANDLER_TAG][CommonConstants.FILENAME_TAG].format(path=CommonConstants.TRAINING_LOG_FOLDER_TAG)

                logging.config.dictConfig(config)
        except Exception as exp:
            cls.logger.error('Exception occured while loading log properties file path :  ' + str(log_properties_file_path))
            raise InitializationException(exp)


    @classmethod
    def get_empty_data_frame_with_specified_columns(cls, column_map, spark):
        try:
            mySchema = StructType([StructField(col, colType) for col, colType in column_map.items()])
            emptyDf = spark.createDataFrame(data=[], schema=mySchema)
            return emptyDf
        except Exception as exp:
            cls.logger.error('Exception occured while getting empty dataframe with specified columns : ' + str(column_map))
            raise DataFrameException(exp)


    @classmethod
    def get_empty_data_frame_without_columns(cls, spark, spark_context):
        try:
            mySchema = StructType([])
            emptyDf = spark.createDataFrame(spark_context.emptyRDD(), mySchema)
            return emptyDf
        except Exception as exp:
            cls.logger.error('Exception occured while getting empty dataframe without columns : ' )
            raise DataFrameException(exp)

    @classmethod
    def get_data_frame_with_specified_columns_and_data(cls, column_map, data, spark):
        try:
            mySchema = StructType([StructField(col, colType) for col, colType in column_map.items()])
            emptyDf = spark.createDataFrame(data=data, schema=mySchema)
            return emptyDf
        except Exception as exp:
            cls.logger.error(
                'Exception occured while getting empty dataframe with specified columns : ' + str(column_map))
            raise DataFrameException(exp)

    @classmethod
    def convert_list_to_comma_separated_string(cls, list_to_convert):
        """
        author: afarooq01@i2cinc.com
        Takes a list and converts it to a string with comma seperated elements of list

        :param list_to_convert:
        :return: string formed from list
        """

        cls.logger.info("List to convert to string: " + str(list_to_convert))
        converted_str = ", ".join(list_to_convert)
        cls.logger.info("String from list: " + converted_str)

        return converted_str

    @classmethod
    def get_list_difference(cls, list1, list2):
        difference = list(set(list1) - set(list2))
        return difference


    @classmethod
    def get_pre_and_post_transformation_feature_names_list(cls, model_features_dictionary):
        """
        author: smahmood@i2cinc.com

        :param model_features_dictionary: value against tag feature_list from model_config
        :return: returns 2 lists, one containing both categorical and continuous feature names combined
                 and another final list with continuous feature names and names of categorical columns containing
                 '_indexed' postfix
        """
        continuous_features_list = model_features_dictionary[CommonConstants.CONTINUOUS_FEATURES_TAG]
        categorical_features_list = model_features_dictionary[CommonConstants.CATEGORICAL_FEATURES_TAG]

        pre_transformation_feature_names_list = continuous_features_list + categorical_features_list

        post_transformation_feature_names_list = []
        for feature_name in categorical_features_list:
            post_transformation_feature_names_list.append(feature_name + '_indexed')
        post_transformation_feature_names_list = post_transformation_feature_names_list + continuous_features_list

        return pre_transformation_feature_names_list, post_transformation_feature_names_list

    @classmethod
    def get_regex_for_replacement(cls, replace_type):
        regex = None
        if replace_type == CommonConstants.REPLACE_TYPE_DIGIT:
            regex = '\d+'
        elif replace_type == CommonConstants.REPLACE_TYPE_SPECIAL_CHARACTER:
            regex = '\W+'
        return regex
        
    @classmethod
    def get_model_id_and_version(cls, model_code, model_code_info_dict):
        model_id_version_dict = model_code_info_dict[int(model_code)]
        model_id = model_id_version_dict['model_id']
        version_id = model_id_version_dict['version_id']
        return model_id, version_id

    def load_and_validate_new_features_list(self, feature_engineering_model_specific_dict):
        self.logger.info(
            "In Class: CommonUtilities, Function: load_and_validate_new_features_list")
        exception_str = " does not exist in service param dictionary"
        self.logger.info("Checking if mandatory key, " + CommonConstants.NEW_FEATURE_LIST_TAG +
                         " exists in param dictionary against flow: " + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
        if CommonConstants.NEW_FEATURE_LIST_TAG not in feature_engineering_model_specific_dict:
            self.logger.error(
                'MissingMandatoryFieldException : Key Error: ' + CommonConstants.NEW_FEATURE_LIST_TAG + exception_str)
            raise MissingMandatoryFieldException(
                'Key Error: ' + CommonConstants.NEW_FEATURE_LIST_TAG + exception_str)
        features_list = feature_engineering_model_specific_dict[CommonConstants.NEW_FEATURE_LIST_TAG]
        self.logger.info(
            "Checking if a value exists against mandatory key, " + CommonConstants.NEW_FEATURE_LIST_TAG
            + " in param dictionary against flow: " + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
        if features_list is None:
            self.logger.error(
                'MissingMandatoryFieldException : Value Error: No value exists for tag: ' + CommonConstants.NEW_FEATURE_LIST_TAG +
                ' for flow: ' + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
            raise MissingMandatoryFieldException(
                'Value Error: No value exists for tag: ' + CommonConstants.NEW_FEATURE_LIST_TAG +
                ' for flow: ' + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)

        self.logger.info(
            "Checking data type of value against key, " + CommonConstants.NEW_FEATURE_LIST_TAG +
            " in param dictionary against flow: " + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
        if not isinstance(features_list, dict):
            self.logger.error('InvalidInfoException : Invalid value for tag: ' +
                              CommonConstants.NEW_FEATURE_LIST_TAG +
                              ' for flow: ' + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
            raise InvalidInfoException('Invalid value for tag: ' +
                                       CommonConstants.NEW_FEATURE_LIST_TAG +
                                       ' for flow: ' + CommonConstants.FEATURE_ENGINEERING_FLOW_STANDARD)
        return features_list.keys()

    @classmethod
    def get_egineered_features_list(self, feature_columns, feature_engineering_model_specific_dict):
        new_features_list = self.load_and_validate_new_features_list(self, feature_engineering_model_specific_dict)
        common_columns_list = list(set(feature_columns) & set(new_features_list))
        self.logger.info("Feature engineer columns are:" + str(common_columns_list))
        return common_columns_list

    @classmethod
    def intersection_of_lists(cls, lst1, lst2):
        lst3 = [value for value in lst1 if value in lst2]
        return lst3
    
    @classmethod
    def check_feature_mappings_existance(self,hdfs_path_mapping):
        """
        author: hrafiq@i2cinc.com

        :param hdfs_path_mapping: hdfs path
        :return: returns True if path exists else False
        """
        try:
            mapping_feature_names = ''
            hdfs_host = re.findall(r'[0-9]+(?:\.[0-9]+){3}', hdfs_path_mapping)
            self.logger.info("Making HDFS client object")
            hdfs = PyWebHdfsClient(host=hdfs_host[0], port=CommonConstants.HDFS_WEB_PORT, user_name='hdfs')
            self.logger.warning("Parsing hdfs path to get the exacr path with IP and PORT")
            path = hdfs_path_mapping.split(CommonConstants.HDFS_PORT)
            path = path[1]
            path = path.replace(CommonConstants.SUB_DIR_MAPPING_TAG + "/", "")
            self.logger.warning("Going to get directory status of hdfs path " + str(path))
            directory_status = hdfs.list_dir(path)
            self.logger.warning("Going to get status of each file in path " + str(path))
            files_status = directory_status['FileStatuses']['FileStatus']
            self.logger.warning("Going to get names of each file ")
            for file in files_status:
                mapping_feature_names += file['pathSuffix'] + ','

            if (CommonConstants.SUB_DIR_MAPPING_TAG in mapping_feature_names):
                return True
            return False

        except Exception as exp:
            self.logger.error('Exception occured while loading feature mapping names from hdfs path ' + str(hdfs_path_mapping))
            raise CommonBaseException(exp)


