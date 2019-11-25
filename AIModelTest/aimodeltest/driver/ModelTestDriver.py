"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains a model test driver, with a class function to run the flow for testing a model on the provided
data.

Class Functions:
test_model

"""

import logging

from pandas import DataFrame

from AICommons.aicommons.dataframeutils.DataFrameUtils import DataFrameUtils
from AICommons.aicommons.machinelearningmodels.AbstractMachineLearningModel import AbstractMachineLearningModel
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.commonutils.CommonValidations import CommonValidations
from AICommons.aicommons.commonutils.CommonUtilities import CommonUtilities
from CommonExceps.commonexceps.DataFrameException import DataFrameException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.MissingMandatoryFieldException import MissingMandatoryFieldException
from CommonExceps.commonexceps.InvalidInfoException import InvalidInfoException
from AIModelTest.aimodeltest.driver.AbstractTestDriver import AbstractTestDriver

from AIModelTest.aimodeltest.utils.Constants import Constants


class ModelTestDriver(AbstractTestDriver):

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)

    def __argument_empty_none_validation(self, test_data, model_params):
        if test_data is None:
            raise MissingMandatoryFieldException("'test_data' argument is None")
        if model_params is None:
            raise MissingMandatoryFieldException("'model_params' argument is None")


    def __argument_type_validation(self, test_data, model_params):
        if not isinstance(test_data, DataFrame):
            raise InvalidInfoException("argument 'test_data' is not of type Pandas Dataframe")
        if not isinstance(model_params, dict):
            raise InvalidInfoException("argument 'model_params' is not of type dictionary")

    def __validate_arguments(self, test_data, model_params):
        try:
            self.__argument_empty_none_validation(test_data, model_params)
            self.__argument_type_validation(test_data, model_params)
        except MissingMandatoryFieldException as exp:
            raise exp
        except InvalidInfoException as exp:
            raise exp

    def test_model(self, test_data, model_params, trained_model):
        """
        Uses trained model to predict for given data

        :param test_data: dataframe of the test data features
        :param model_params: configurations of the model
        :param trained_model: A trained model instance to be used on the test data
        :return: An array of the target predictions
        """

        try:
            self.logger.info("Validating input test data and model params")
            self.__validate_arguments(test_data, model_params)
            CommonValidations.validate_model_params(model_params)

            self.logger.info("Validating test data features are present in the required features' list")
            CommonValidations.validate_data_features_against_model(test_data, model_params[CommonConstants.FEATURE_LIST_TAG])

            #Todo Validating a model for diff api's

            # # self.logger.info("Validating input trained_model")
            #  CommonValidations.validate_pipeline_model('trained_pipeline', trained_model)
            # # Validate a trained model instance instead

            self.logger.warning("Going to predict using trainied model for test data on columns: " +
                                str(test_data.columns))
            predicted_data = AbstractMachineLearningModel.predict(model=trained_model, data=test_data, params_dict= model_params)
            self.logger.warning("Predictions successfully made")

            self.logger.warning("Returning predicted data")
            return predicted_data

        except MissingMandatoryFieldException as exp:
            raise CommonBaseException(exp)
        except InvalidInfoException as exp:
            raise CommonBaseException(exp)
        except DataFrameException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            self.logger.error('Exception occured while testing model_params = ' + str(
                model_params) + ' model = ' + str(trained_model))
            raise CommonBaseException(exp)


