"""
    Created By: Ramsha Siddiqui
    Description: This is the Abstract Config Parser Class -
    it deals with Parsing a Config File: Open, Read, Write, etc.
"""

from configparser import ConfigParser
import os
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

    def read(self, args):
        return self.cls_config_parser.read_dict(args)

    @abc.abstractmethod
    def parse(self):
        pass
