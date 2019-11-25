"""
Authors: smunawar02@i2cinc.com

Purpose:
This file contains Data Training and Testing Handler class that will handle training and prediction of the model.

"""
import logging
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from AICommons.aicommons.commonutils.CommonUtilities import CommonUtilities
from AICommons.aicommons.hdfsutils.HDFSUtils import HDFSUtils
from AICommons.aicommons.dao.AbstractMachineLearningModelDAOFactory import AbstractMachineLearningModelDAOFactory
from AICommons.aicommons.dataframeutils.DataFrameUtils import DataFrameUtils
from pipeline.utils.Constants import Constants
from AIModelTest.aimodeltest.driver.AbstractTestDriverFactory import AbstractTestDriverFactory
from AIModelTrain.aimodeltrain.driver.AbstractTrainDriverFactory import AbstractTrainDriverFactory
from CommonExceps.commonexceps.SQLException import SQLException
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException
from CommonExceps.commonexceps.DataFrameException import DataFrameException


class ModelDataTrainingAndTestingHandler:

    def __init__(self):
        self.logger = logging.getLogger(Constants.LOGGER_NAME)



    def perform_model_training(self, train_df, target, model_parameters, model_hyper_parameters, model_cross_validator_params):
        """

        :param train_df:
        :param target:
        :param model_parameters:
        :param model_hyper_parameters:
        :param model_cross_validator_params:
        :return a trained model instance:
        """
        train_service_handler = None
        try:
            #todo: save trained model instance against the model and version id's on hdfs and its path in informix
            self.logger.warning("Getting an instance of the train driver for model name: " + str(model_parameters[CommonConstants.MODEL_NAME_TAG]))
            train_service_handler = AbstractTrainDriverFactory.get_instance(model_parameters[CommonConstants.MODEL_NAME_TAG])

            print(train_df)
            self.logger.warning("Going to train model on train_df")
            trained_model = train_service_handler.train_model(data=train_df, target=target, model_params=model_parameters, model_hyper_params=model_hyper_parameters,
                                                              model_cross_validator_params=model_cross_validator_params)

            return trained_model

        except SQLException as exp:
            raise exp
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            self.logger.error('Exception occured while performing model training')
            raise CommonBaseException(exp)

    def perform_model_testing(self, test_data, model_parameters, trained_model):
        """

        :param test_data:
        :param model_parameters:
        :param trained_model:
        :return: An array of the target predictions
        """

        test_service_handler = None
        try:
            # todo: Persist the predicted results in the DB against the model and version id's.

            self.logger.warning("Getting an instance of the test driver for model name: " + str(model_parameters[CommonConstants.MODEL_NAME_TAG]))
            test_service_handler = AbstractTestDriverFactory.get_instance(model_parameters[CommonConstants.MODEL_NAME_TAG])
            self.logger.warning("Going to test the trained model on test data")
            prediction_df = test_service_handler.test_model(test_data=test_data, model_params=model_parameters, trained_model=trained_model)

            return prediction_df

        except CommonBaseException as exp:
            raise exp
        except SQLException as exp:
            raise CommonBaseException(exp)
        except Exception as exp:
            self.logger.error('Exception occured while performing model testing')
            raise CommonBaseException(exp)

