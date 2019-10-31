"""
    Created By: Ramsha Siddiqui
    Description: This is the Abstract Config Parser Class -
    it deals with Parsing a Config File: Open, Read, Write, etc.
"""

from configparser import ConfigParser
import yaml
import abc
from commons.config.AbstractConfig import AbstractConfig


class AbstractConfigParser(metaclass=abc.ABCMeta):

    def __init__(self):
        self.cls_config_parser = ConfigParser(allow_no_value=True)
        self.cls_config_pattern = AbstractConfig()
        self.cls_config_file_path = None

    @property
    def config_pattern(self):
        return self.cls_config_pattern

    @config_pattern.setter
    def config_pattern(self, args):
        self.cls_config_pattern = args

    @property
    def config_parser(self):
        return self.cls_config_parser

    @config_parser.setter
    def config_parser(self, args):
        self.cls_config_parser = args

    def write(self, args):
        self.cls_config_file_path = args
        with open(self.cls_config_file_path, 'w') as file:
            self.cls_config_parser.write(file)

    def read_config(self, args):
        self.cls_config_parser.read(args)

        self.cls_config_pattern.id, self.cls_config_pattern.name, properties, methods, self.cls_config_pattern.vars = \
            self.cls_config_parser[AbstractConfig.__name__].values()

        properties = yaml.safe_load(properties)
        methods = yaml.safe_load(methods)

        self.cls_config_pattern.properties.req_args, self.config_pattern.properties.req_input, \
            self.cls_config_pattern.properties.req_data, self.cls_config_pattern.properties.parents, \
            self.cls_config_pattern.properties.children = [None if x == 'None' else x for x in properties.values()]

        self.cls_config_pattern.methods.static_methods, self.cls_config_pattern.methods.impl_methods, \
            self.cls_config_pattern.methods.abs_methods = [None if x == 'None' else x for x in methods.values()]

    def read_dict(self, args):
        return self.cls_config_parser.read_dict(args)

    @abc.abstractmethod
    def parse(self):
        pass
