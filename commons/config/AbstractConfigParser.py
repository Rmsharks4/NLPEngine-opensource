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

    @classmethod
    def initialize(cls, args):
        cls.configFilePath = (os.path.join(os.getcwd(), args))

    @classmethod
    def write(cls, args):
        cls.configParser.write(args)

    @classmethod
    def read(cls, args):
        return cls.configParser.read(args)

    @abc.abstractmethod
    def parse(self, args):
        pass
