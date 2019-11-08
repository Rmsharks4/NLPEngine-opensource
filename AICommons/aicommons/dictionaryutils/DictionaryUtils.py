
import logging
from AICommons.aicommons.utils.Constants import Constants
from AICommons.aicommons.commonutils.CommonConstants import CommonConstants
from CommonExceps.commonexceps.CommonBaseException import CommonBaseException

class DictionaryUtils:
    """
    Implement the operations to create concrete product objects.
    """

    logger = logging.getLogger(Constants.LOGGER_NAME)

    @classmethod
    def merge_and_overwrite_dicts(cls, *dict_args):
        """
        author: afarooq01@i2cinc.com
        Given any number of dicts, shallow copy and merge into a new dict,
            precedence goes to key value pairs in latter dicts.

        :param base_dict: dictionary with original values
        :param overwrite_dict: dictionary with va;ues to overwrite
        :return: the new merged dictionary with updated/overwritten values
        """
        try:
            result = {}

            cls.logger.info("Merging the dictionaries: ")
            for dictionary in dict_args:
                result.update(dictionary)

            cls.logger.info("Merged dictionary: " + str(result))
            return result
        except Exception as exp:
            cls.logger.error('Exception occured while merging and overwriting dicts ')
            raise CommonBaseException(exp)

    @classmethod
    def convert_dict_values_to_list(cls, params_dict):
        """
        author: hrafiq@i2cinc.com
        Given dict , convert all non-list values to list

        :param params_dict: dictionary with original values
        :return: the updated dict
        """
        try:
            for key,value in params_dict.items():
                if key is not CommonConstants.NUM_FOLDS_TAG:
                    if not isinstance(value, list):
                        params_dict[key] = [value]
            return params_dict

        except Exception as exp:
            cls.logger.error('Exception occured while converting dict values to list ')
            raise CommonBaseException(exp)
