
import logging.config

from aicommonspython.commonutils.CommonConstants import CommonConstants
from aicommonspython.machinelearningmodels.AbstractMachineLearningModelFactory import AbstractMachineLearningModelFactory

from aicommonspython.dao.AbstractMachineLearningModelDAOFactory import AbstractMachineLearningModelDAOFactory
from commonexceps.SQLException import SQLException
from commonexceps.CommonBaseException import CommonBaseException
from commonexceps.HDFSException import HDFSException
from aicommonspython.commonutils.CommonUtilities import CommonUtilities
from aicommonspython.utils.Constants import Constants
from pyspark.ml import PipelineModel
from pywebhdfs.webhdfs import PyWebHdfsClient
import re

class HDFSUtils:

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def _get_loadable_pipeline_object(cls):


        """
        :return: pipeline model load object
        """

        cls.logger.info("Returning pipeline model object")
        return PipelineModel(stages=[])

    @classmethod
    def _make_hdfs_path(cls, base_path, model_type, model_id, model_version, sub_dir_type):
        """
         author: afarooq01@i2cinc.com
         Makes path for a specific HDFS destination by appending strings

        :param base_path: Base HDFS path
        :param model_type: Model type  (machine_learning_models, transformations etc.)
        :param model_id:
        :param model_version:
        :return: an hdfs path formed by concatenating above parameters
        """

        cls.logger.info("Making HDFS path by concatenating strings ")
        cls.logger.debug("BASE HDFS path: " + str(base_path))
        cls.logger.debug("Model type: " + str(model_type))
        cls.logger.debug("Model id: " + str(model_id))
        cls.logger.debug("Model version: " + str(model_version))
        path = str(base_path) + "/" + str(model_type) + "/" + str(model_id) + "/" + str(model_version) + "/" + str(sub_dir_type) + "/"
        cls.logger.info("HDFS Path: " + str(path))

        return path

    @classmethod
    def _load_mapping_feature_names(cls, hdfs_path):
        """
         author: hrafiq@i2cinc.com
         Loads the feature mapping names from hdfs

        :param hdfs_path_mapping:  HDFS path on which feature mapping is stored
        :return: string of mapping_feature names
        """
        path = ""
        try:

            mapping_feature_names = ''

            cls.logger.warning("Getting ip address from base hdfs path")
            hdfs_host = re.findall(r'[0-9]+(?:\.[0-9]+){3}',hdfs_path)
            cls.logger.info("Making HDFS client object")
            hdfs = PyWebHdfsClient(host=hdfs_host[0], port=CommonConstants.HDFS_WEB_PORT, user_name='hdfs')
            cls.logger.warning("Parsing hdfs path to get the exacr path with IP and PORT")
            path = hdfs_path.split(CommonConstants.HDFS_PORT)
            path = path[1]
            cls.logger.warning("Going to get directory status of hdfs path " + str(path))
            directory_status = hdfs.list_dir(path)
            cls.logger.warning("Going to get status of each file in path " + str(path))
            files_status = directory_status['FileStatuses']['FileStatus']
            cls.logger.warning("Going to get names of each file ")

            for file in files_status:
                mapping_feature_names += file['pathSuffix'] + ','
            cls.logger.warning("Removing last comma from comma separated string ")
            mapping_feature_names = mapping_feature_names[:-1]

            cls.logger.info("File names loaded successfully.")
            cls.logger.info("File names : " + str(mapping_feature_names))

            return mapping_feature_names
        except Exception as exp:
            cls.logger.error('Exception occured while loading feature mapping names from hdfs path ' + str(path))
            raise CommonBaseException(exp)

    @classmethod
    def save_to_hdfs_and_informix(cls, base_path, model_code, model_id, model_version, model, informix_multi_instance):
        """
        author: afarooq01@i2cinc.com
        Save model to hdfs; first gets model_id and model_version against model_code; then formulates an hdfs path
        against these value and then saves the model to that path, and saves the path back into informix db

        :param base_path: base/root path from HDFS
        :param model_code:
        :param model_id: a unique identifier for the model made
        :param model_version:
        :param model: trained model object
        :param informix_multi_instance: informix mi instance
        :return:
        """
        hdfs_path = None
        try:
            cls.logger.info("Getting object of DAO Factory class")
            dao_obj = AbstractMachineLearningModelDAOFactory()
            cls.logger.info("Object retrieved")

            cls.logger.info("Getting dao instance for database: " + str(CommonConstants.DATABASE_HDFS))
            hdfs_dao = dao_obj.get_machine_learning_model_dao(CommonConstants.DATABASE_HDFS)
            cls.logger.info("Instance retrieved")
            hdfs_path_pipeline = ''
            cls.logger.warning("Checking if model is of type Pipeline model ")
            if isinstance(model, PipelineModel):
                cls.logger.info("Going to make HDFS path to save model")
                hdfs_path_pipeline = HDFSUtils._make_hdfs_path(base_path,
                                                            CommonConstants.HDFS_MACHINE_LEARNING_MODELS_PATH_TAG,
                                                            model_id, model_version, CommonConstants.SUB_DIR_PIPELINE_TAG)
                cls.logger.info("HDFS path made: " + str(hdfs_path_pipeline))

                cls.logger.warning("Going to save model to the HDFS path: " + str(hdfs_path_pipeline))
                # hdfs_dao.save(hdfs_path, model)
                model.save(hdfs_path_pipeline)
                cls.logger.warning("Model successfully saved to the HDFS path: " + str(hdfs_path_pipeline))

            cls.logger.info("Going to make HDFS path to get feature mappings")
            hdfs_path_mapping = HDFSUtils._make_hdfs_path(base_path,
                                                        CommonConstants.HDFS_MACHINE_LEARNING_MODELS_PATH_TAG,
                                                        model_id, model_version, CommonConstants.SUB_DIR_MAPPING_TAG)

            cls.logger.warning("Checking if feature mappings exists in hdfs path: " + str(hdfs_path_mapping) + "  for model_id: " + str(model_id) +" version_id: " + str(model_version))

            if(CommonUtilities.check_feature_mappings_existance(hdfs_path_mapping) is True):
                cls.logger.warning("Going to load all mapping_feature names from the HDFS path: " + str(hdfs_path_mapping))
                mapping_feature_names = HDFSUtils._load_mapping_feature_names(hdfs_path_mapping)
            else:
                cls.logger.warning("Feature mappings does not exist in hdfs path: " + str(
                    hdfs_path_mapping) + "  for model_id: " + str(model_id) + " version_id: " + str(model_version))
                mapping_feature_names = None

            cls.logger.info("Getting dao instance for database: " + str(CommonConstants.DATABASE_INFORMIX))
            informix_dao = dao_obj.get_machine_learning_model_dao(CommonConstants.DATABASE_INFORMIX)
            cls.logger.info("Instance retrieved")
            if isinstance(model, PipelineModel):
                cls.logger.warning("Going to write hdfs model path to Informix DB: " + str(hdfs_path_pipeline))
                informix_dao.write_path_and_mapping_features(hdfs_path_pipeline, model_code, mapping_feature_names, informix_multi_instance)
                cls.logger.warning("Model path successfully saved to Informix DB: " + str(hdfs_path_pipeline))

            else:
                cls.logger.warning("Going to write hdfs model path to Informix DB: " + str(hdfs_path_mapping))
                informix_dao.write_path_and_mapping_features(hdfs_path_mapping, model_code, mapping_feature_names,
                                                             informix_multi_instance)
                cls.logger.warning("Model path successfully saved to Informix DB: " + str(hdfs_path_mapping))

        except SQLException as exp:
            raise exp
        except HDFSException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            cls.logger.error('Exception occured while saving model to hdfs ' + str(hdfs_path))
            raise CommonBaseException(exp)

    @classmethod
    def load_model_from_hdfs(cls, path, model_name):
        """
        author: afarooq01@i2cinc.com
        Load the model from given path, by first taking the model_name and getting the appropriate model load object for
        it and then loads the model from hdfs into that load object

        :param path: hdfs path
        :param model_name: the actual model name (decision_tree, random_forest etc)
        :return: loaded model
        """

        try:
            cls.logger.info("Getting object of DAO Factory class")
            dao_obj = AbstractMachineLearningModelDAOFactory()
            cls.logger.info("Object retrieved")

            cls.logger.info("Getting dao instance for database: " + str(CommonConstants.DATABASE_HDFS))
            hdfs_dao = dao_obj.get_machine_learning_model_dao(CommonConstants.DATABASE_HDFS)
            cls.logger.info("Instance retrieved")

            cls.logger.info("Getting object of Machine Learning Model Factory class")
            model_class = AbstractMachineLearningModelFactory()
            cls.logger.info("Object retrieved")

            cls.logger.info("Getting model class implementation for : " + str(model_name))
            model_class = model_class.get_instance(model_name)
            cls.logger.info("Model class implementation successfully obtained")

            cls.logger.info("Going to load pipeline model " + str(model_name) + " from the HDFS path: " + str(path))
            model_obj = model_class.get_loadable_object()
            cls.logger.info("Model load object successfully retrieved")

            cls.logger.warning("Going to load model: " + str(model_name) + " from the HDFS path: " + str(path))
            loaded_model = hdfs_dao.load(path, model_obj)
            cls.logger.warning("Model of: " + str(model_name) + " successfully loaded from path: " + str(path))

            return loaded_model
        except HDFSException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            cls.logger.error('Exception occured while loading model ' + str(model_name) + ' from hdfs '+ str(path))
            raise CommonBaseException(exp)

    @classmethod
    def load_pipeline_from_hdfs(cls, path):
        """
        author: afarooq01@i2cinc.com
        Load the model from given path, by first taking the model_name and getting the appropriate model load object for
        it and then loads the model from hdfs into that load object

        :param path: hdfs path
        :param model_name: the actual model name (decision_tree, random_forest etc)
        :return: loaded model
        """

        try:
            cls.logger.info("Getting object of DAO Factory class")
            dao_obj = AbstractMachineLearningModelDAOFactory()
            cls.logger.info("Object retrieved")

            cls.logger.info("Getting dao instance for database: " + str(CommonConstants.DATABASE_HDFS))
            hdfs_dao = dao_obj.get_machine_learning_model_dao(CommonConstants.DATABASE_HDFS)
            cls.logger.info("Instance retrieved")

            cls.logger.info("Going to load pipeline model ")
            model_obj = HDFSUtils._get_loadable_pipeline_object()
            cls.logger.info("Model load object successfully retrieved")

            cls.logger.warning("Going to load Pipeline model the HDFS path: " + str(path))

            # loaded_model = hdfs_dao.load(path, model_obj)
            loaded_model = PipelineModel.read().load(path)
            cls.logger.warning("Pipeline model  successfully loaded from path: " + str(path))

            return loaded_model
        except HDFSException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            cls.logger.error('Exception occured while loading model from hdfs ' + str(path))
            raise CommonBaseException(exp)

    @classmethod
    def load_feature_mapping_dict_from_hdfs(cls, path, model_mapping_features_list):
        """
        author: uahmad@i2cinc.com
        Load the hitrate dict from given path

        :param path: hdfs path
        :return: loaded dict
        """

        try:
            model_mapping_dict = {}
            cls.logger.warning("Going to load feature mappings for: " + str(model_mapping_features_list) + " from hdfs path: " + str(path))
            if model_mapping_features_list is None:
                cls.logger.error("Model mapping feature list is empty/null for path: " + str(path))
                raise CommonBaseException("Model mapping feature list is empty/null for path: " + str(path))

            for mapping_name in model_mapping_features_list:
                if not mapping_name.endswith('_histogram'):
                    cls.logger.warning("Going to load mapping: " + str(mapping_name) + " from path: " + str(path))
                    json_df = CommonConstants.SPARK_SESSION.read.json(path + mapping_name)
                    model_mapping_dict[mapping_name] = json_df.rdd.collectAsMap()
            return model_mapping_dict
        except HDFSException as exp:
            raise CommonBaseException(exp)
        except CommonBaseException as exp:
            raise exp
        except Exception as exp:
            cls.logger.error('Exception occured while loading dict from hdfs ' + str(path))
            raise CommonBaseException(exp)

