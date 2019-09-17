"""
    Created By: Ramsha Siddiqui
    Description: This is the factory class for Abstract Config Parser
"""

from commons.config.PreProcessingConfigParserImpl import PreProcessingConfigParserImpl
from constants import constants


class AbstractConfigParserFactory:

    @classmethod
    def get_config_parser(cls, parser_type):
        switcher = {
            PreProcessingConfigParserImpl(): constants.PREPROCESSING_CONFIG_PARSER_IMPL
        }

        return switcher.get(parser_type, '')
