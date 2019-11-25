from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.commonutils.CommonUtilities import CommonUtilities

from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
import logging
from AICommons.aicommons.utils.Constants import Constants



class CommonValidations:
    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def validate_model_params(cls, model_params):

        if CommonConstants.MODEL_NAME_TAG not in model_params or not model_params.get(CommonConstants.MODEL_NAME_TAG):
            cls.logger.error("MissingMandatoryFieldException : " +str(CommonConstants.MODEL_NAME_TAG) + " key does not exist in " +
                                                 "'model_params' or has no value assigned " )
            raise MissingMandatoryFieldException(str(CommonConstants.MODEL_NAME_TAG) + " key does not exist in " +
                                                 "'model_params' or has no value assigned ")
        elif not isinstance(model_params[CommonConstants.MODEL_NAME_TAG], str):
            cls.logger.error("InvalidInfoException : "+str(CommonConstants.MODEL_NAME_TAG) + ' value is not of type string')
            raise InvalidInfoException(str(CommonConstants.MODEL_NAME_TAG) + ' value is not of type string')
        if CommonConstants.FEATURE_LIST_TAG not in model_params or not model_params[CommonConstants.FEATURE_LIST_TAG]:
            cls.logger.error("MissingMandatoryFieldException : " + str(CommonConstants.FEATURE_LIST_TAG) + " key does not exist in " +
                                                 "'model_params' or has no value assigned ")
            raise MissingMandatoryFieldException(str(CommonConstants.FEATURE_LIST_TAG) + " key does not exist in " +
                                                 "'model_params' or has no value assigned ")
        elif not isinstance(model_params[CommonConstants.FEATURE_LIST_TAG], list):
            cls.logger.error("InvalidInfoException : " + str(CommonConstants.FEATURE_LIST_TAG) + ' value is not of type list')
            raise InvalidInfoException(str(CommonConstants.FEATURE_LIST_TAG) + ' value is not of type list')
        return

    @classmethod
    def validate_data_features_against_model(cls, data, features_list):
        model_features_not_in_data = CommonUtilities.get_list_difference(features_list,
                                                                         data.columns)
        if len(model_features_not_in_data) > 0:
            cls.logger.error("InvalidInfoException : Features: " + str(model_features_not_in_data) + " not found in received data " +
                                       "but required by the model" )
            raise InvalidInfoException("Features: " + str(model_features_not_in_data) + " not found in received data " +
                                       "but required by the model")
        return

    @classmethod
    def validate_dict_for_empty_values(cls,_dict):
        for key, value in _dict.items():
            if value is None:
                cls.logger.error('InvalidInfoException : Null or empty value received against dictionary key: ' + str(key))
                raise InvalidInfoException('Null or empty value received against dictionary key: ' + str(key))


    @classmethod
    def validate_pipeline_model(cls, model_name, pipeline_model):
        """
        author: smahmood@i2cinc.com
        Validates that input pipeline model is not null and belongs to the correct datatype

        :param pipeline_model_name: Name of given pipeline model
        :param pipeline_model: Pipeline
        :return: --
        """
        if pipeline_model is None:
            cls.logger.error("MissingMandatoryFieldException" + model_name + " is Missing")
            raise MissingMandatoryFieldException(model_name + " argument is None")

        if not isinstance(pipeline_model, PipelineModel) and not isinstance(pipeline_model, Pipeline):
            cls.logger.error('InvalidInfoException : "Invalid type for argument '+ model_name)
            raise InvalidInfoException("Invalid type for argument "+ model_name)

    @classmethod
    def validate_model_id_and_version(cls, model_code, model_id, version_id):

        if (model_id is None) | (version_id is None):
            cls.logger.error(
                'CommonBaseException : model_id is None or version_id is None against model_code: ' + str(
                    model_code))
            raise CommonBaseException(
                'model_id is None or version_id is None against model_code: ' + str(model_code))

        cls.logger.warning(
            "For model_code: " + str(model_code) + " model_id: " + str(model_id) + " version_id: " + str(
                version_id))

