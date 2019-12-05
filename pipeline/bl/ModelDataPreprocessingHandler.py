import logging
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.SQLException import SQLException
from preprocessing.driver.PreProcessorService import PreProcessorService


class ModelDataPreprocessingHandler:

    def __init__(self):
        self.logger = logging.getLogger(CommonConstants.PREPROCESSING_LOGGER_NAME)

    def perform_data_preprocessing(self, postgre_spark_prop, raw_data_df, driver_config_dict, preprocessing_flow_version, preprocessing_model_specific_dict, persist_query, model_id, version_id, model_code, train_test_prediction_mode, database_metadata_dict, engineered_features_list,is_db_save = '1'):
        """

        :param postgre_spark_prop: spark connection
        :param raw_data_df: financial df
        :param transformation_pipeline: transformation pipeline for online mode
        :return: preprocessed data and pipeline for string indexer
        """
        preprocess_service = None
        try:
            """
            okay so here i call the run function of my PreProcessing Service and pass it the following configurations:
            2. Per Model Requirements - preprocess operations required by each model in their specific order.
                i. model-id: lowercase, lemmatize, stem
            3. Raw Input Data - passed as input
            4. Mode - Predict, or test/train
            """

        except CommonBaseException as exp:
            raise exp
        except SQLException as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            self.logger.error('Exception occured while performing data preprocessing')
            raise CommonBaseException(exp)