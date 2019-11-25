
"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains a model train driver, with a class function to run the flow for training a model on provided data.

Class Functions:
train_model

"""

from AICommons.aicommons.machinelearningmodels.AbstractMachineLearningModelFactory import AbstractMachineLearningModelFactory
from AIModelTrain.aimodeltrain.driver.AbstractTrainDriver import AbstractTrainDriver
from AICommons.aicommons.dataframeutils.DataFrameUtils import DataFrameUtils
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.commonutils.CommonUtilities import CommonUtilities
from AICommons.aicommons.dictionaryutils.DictionaryUtils import DictionaryUtils
from AICommons.aicommons.commonutils.CommonValidations import CommonValidations
import logging
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.InitializationException import InitializationException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from AIModelTrain.aimodeltrain.utils.Constants import Constants

from pandas import DataFrame


class ModelTrainDriver(AbstractTrainDriver):

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def __argument_empty_none_validation(self, data, model_params, model_hyper_params, model_cross_validator_params):
        if data is None:
            self.logger.error("MissingMandatoryFieldException : 'data' argument is None")
            raise MissingMandatoryFieldException("'data' argument is None")
        if model_params is None:
            self.logger.error("MissingMandatoryFieldException : 'model_params' argument is None")
            raise MissingMandatoryFieldException("'model_params' argument is None")
        elif model_params[CommonConstants.ENABLE_CV_TAG] == 'Y' and model_cross_validator_params is None:
            self.logger.error("MissingMandatoryFieldException : 'model_cross_validator_params' argument "
                              "is None but cross validation is enabled ")
            raise MissingMandatoryFieldException("'model_cross_validator_params' argument is None")
        if model_hyper_params is None:
            self.logger.error("MissingMandatoryFieldException : 'model_hyper_params' argument is None")
            raise MissingMandatoryFieldException("'model_hyper_params' argument is None")

    def __argument_type_validation(self, data, model_params, model_hyper_params, model_cross_validator_params):
        if not isinstance(data, DataFrame):
            self.logger.error("InvalidInfoException : argument 'data' is not of type 'Pandas DataFrame'")
            raise InvalidInfoException("argument 'data' is not of type 'Pandas DataFrame'")
        if not isinstance(model_params, dict):
            self.logger.error("InvalidInfoException : argument 'model_params' is not of type dictionary")
            raise InvalidInfoException("argument 'model_params' is not of type dictionary")
        if not isinstance(model_hyper_params, dict):
            self.logger.error("InvalidInfoException : argument 'model_hyper_params' is not of type dictionary")
            raise InvalidInfoException("argument 'model_hyper_params' is not of type dictionary")
        if not isinstance(model_cross_validator_params, dict):
            self.logger.error("InvalidInfoException : argument 'model_cross_validator_params' is not of type dictionary")
            raise InvalidInfoException("argument 'model_cross_validator_params' is not of type dictionary")

    def __validate_arguments(self, data, model_params, model_hyper_params, model_cross_validator_params):
        try:
            self.__argument_empty_none_validation(data, model_params, model_hyper_params, model_cross_validator_params)
            self.__argument_type_validation(data, model_params, model_hyper_params, model_cross_validator_params)
        except MissingMandatoryFieldException as exp:
            raise exp
        except InvalidInfoException as exp:
            raise exp

    def train_model(self, data, target, model_params, model_hyper_params, model_cross_validator_params):
        """
        :param data: dataframe of the training data features
        :param target: outcome associated with the training data features
        :param model_params: The model configurations
        :param model_hyper_params: Hyper-parameter settings to train the model on
        :param model_cross_validator_params:
        :return: trained model
        """
        try:

            self.logger.warning("Validating the arguments")
            self.__validate_arguments(data, model_params, model_hyper_params,model_cross_validator_params)

            self.logger.warning("Validating the model parameters")
            CommonValidations.validate_model_params(model_params)

            self.logger.info("Getting model class implementation for: " + str(model_params[CommonConstants.MODEL_NAME_TAG]))
            model_class = AbstractMachineLearningModelFactory.get_instance(
                model_name=model_params[CommonConstants.MODEL_NAME_TAG])
            self.logger.info("Model class implementation successfully obtained")

            self.logger.info("Getting default params dict for the specific class")
            default_params_dict = model_class.get_default_params()
            self.logger.info("Default params retrieved: " + str(default_params_dict))

            if (model_params.get(CommonConstants.ENABLE_CV_TAG, None) is None) or \
                    (model_params[CommonConstants.ENABLE_CV_TAG] != 'Y'):
                self.logger.info(
                    "Going to merge these dictionaries for model parameters: " + "default params dictionary: " +
                    str(default_params_dict) + "model_hyper_params: " +
                    str(model_hyper_params) + "model_params: " + str(model_params))
                merged_params_dict = DictionaryUtils.merge_and_overwrite_dicts(default_params_dict, model_hyper_params,
                                                                               model_params)
                self.logger.info("Merged params dictionary: " + str(merged_params_dict))

            else:

                self.logger.info(
                    "Going to merge these dictionaries for model parameters: " + "default params dictionary: " +
                    str(default_params_dict) + "cross_validation_hyper_params: " +
                    str(model_cross_validator_params) + "model_params: " + str(model_params))
                merged_params_dict = DictionaryUtils.merge_and_overwrite_dicts(default_params_dict, model_hyper_params,
                                                                         model_cross_validator_params, model_params)
            self.logger.warning("Validating merged_params_dict for empty values")
            CommonValidations.validate_dict_for_empty_values(merged_params_dict)

            self.logger.warning("Initializing model object from class implementation of: " +
                                str(model_params[CommonConstants.MODEL_NAME_TAG]) + " with parameters: "
                                + str(merged_params_dict))
            model = model_class.initialize_model(params_dict=merged_params_dict)
            self.logger.warning("Model object initialized" + " with target column: " + "'" + CommonConstants.TARGET_COLUMN_TAG
                                + "'"+ " with parameters: " + str(model_class.get_model_params(model)))

            if (model_params.get(CommonConstants.ENABLE_CV_TAG, None) is None) or \
                    (model_params[CommonConstants.ENABLE_CV_TAG] != 'Y'):
                self.logger.warning("Going to train the model")
                trained_model = model_class.train(model=model, data=data, target=target, params_dict= merged_params_dict)
                self.logger.warning("model successfully trained")
            else:
                self.logger.warning("Going to perform Cross Validation for selecting the best model")
                trained_model = model_class.perform_cross_validation(model=model, data=data, target=target,
                                                                     params_dict=merged_params_dict)
                self.logger.warning("Cross Validation for the model " + str(model_params[CommonConstants.MODEL_NAME_TAG]) + " completed successfully")

            # TODO: return and save trained_pipeline on hdfs
            return trained_model

        except MissingMandatoryFieldException as exp:
            raise CommonBaseException(exp)
        except InvalidInfoException as exp:
            raise CommonBaseException(exp)
        except DataFrameException as exp:
            raise CommonBaseException(exp)
        except InitializationException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            self.logger.error('Exception occured while training model on model_params = ' + str(model_params) +
                              'model_hyper_params= ' + str(model_hyper_params))
            raise CommonBaseException(exp)

