"""
    Created By: Ramsha Siddiqui
    Description: This is the factory class for Abstract Config Parser
"""
from commons.config.StandardConfigParserImpl import StandardConfigParserImpl


class AbstractConfigParserFactory:

    @classmethod
    def get_config_parser(cls, parser_type):
        switcher = {
            StandardConfigParserImpl.__name__: StandardConfigParserImpl()
        }

        return switcher.get(parser_type, '')
