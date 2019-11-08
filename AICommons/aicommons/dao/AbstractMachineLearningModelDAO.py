"""
Authors: afarooq01@i2cinc.com.

Purpose:
This file contains an abstract class with the abstract function(s) that all database DAOs need to implement.

Abstract Functions:
read_query
write_query

"""

import logging

from abc import ABC

from AICommons.aicommons.utils.Constants import Constants


class AbstractMachineLearningModelDAO(ABC):
    """
    An abstract class to create different DAOs for different types of databases
    """

    _READ_PRE_PROCESSED_AND_ENGINEERED_DATA = """
    (
    select ai_preprocessed.{}, {}, {}
    from {}.ai_feature_engineered inner join {}.ai_preprocessed
    on ai_feature_engineered.trace_audit_no = ai_preprocessed.trace_audit_no
    where ai_preprocessed.{} = '{}'
    )
    as df
    """

    #
    # _READ_PRE_PROCESSED_AND_ENGINEERED_DATA_SAMPLED = """
    # (
    # select ai_preprocessed_sampled.{}, {}, {}
    # from {}.ai_feature_engineered_sampled inner join {}.ai_preprocessed_sampled
    # on ai_feature_engineered_sampled.trace_audit_no = ai_preprocessed_sampled.trace_audit_no
    # where ai_preprocessed_sampled.{} = '{}'
    # )
    # as df
    # """

    _GET_MODEL_ID_AND_VERSION = """
    select model_id, version_id 
    from ai_model1s 
    where model_code = ? 
    """

    _CHECK_IS_GRP_BASED = """
    select is_grp_based
    from ai_models
    where model_id = ?
    """

    _WRITE_MODEL_PATH = """
    UPDATE ai_model1s 
    SET model_path= ?,
     mapping_features = ?
    WHERE model_code = ? 
    """

    _READ_MODEL_PATH = """
    SELECT model_path, mapping_features
    FROM ai_model1s 
    WHERE model_code = ?
    """

    _READ_ALL_VALID_MODEL_PATHS = """
        SELECT model_code, model_path, mapping_features
        FROM ai_model1s 
        WHERE model_path IS NOT NULL
        AND model_path <> ''
        """
    _READ_ALL_MODEL_ID_AND_VERSION = """
    SELECT model_code, model_id, version_id
    FROM ai_model1s
    """

    _GET_MODEL_CODE_GROUP = """
    SELECT sub_model_code FROM ai_model_grps WHERE model_code = ?
    """

    def read_processed_and_engineered_data(self, feature_list, model_code, schema, database_connection):
        pass

    def write_model_path(self, path, model_code, database_connection):
        pass

    def read_model_path_and_mapping(self, model_code, multi_instance_id):
        pass

    def write_predictions(self, predicted_data, model_code, query, schema, database_connection,model_params):
        pass

    def read_all_valid_model_paths(self, multi_instance_id):
        pass

    def write_anomaly_scores(self, df, model_code, query, schema, database_connection, model_params):
        pass
