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
        self.config_parser = ConfigParser(allow_no_value=True)
        self.config_pattern = AbstractConfig()
        self.config_file_path = None

    @property
    def config_pattern(self):
        return self.config_pattern

    @config_pattern.setter
    def config_pattern(self, args):
        self.config_pattern = args

    @property
    def config_parser(self):
        return self.config_parser

    @config_parser.setter
    def config_parser(self, args):
        self.config_parser = args

    def write(self, args):
        self.config_file_path = args
        with open(self.config_file_path, 'w') as file:
            self.config_parser.write(file)

    def read(self, args):
        return self.config_parser.read(args)

    @abc.abstractmethod
    def parse(self, args):
        pass
