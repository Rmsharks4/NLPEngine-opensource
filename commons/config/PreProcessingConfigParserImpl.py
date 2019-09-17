"""
    Created By: Ramsha Siddiqui
    Description: This is an implementation of the Abstract Config Parser Class -
    we implement the configurations of Pre-Processing in this one ...
"""

from commons.config.AbstractConfigParser import AbstractConfigParser
from types import FunctionType


class PreProcessingConfigParserImpl(AbstractConfigParser):

    def __init__(self):
        super().__init__()
        self.init_config()

    def init_config(self):
        self.config_pattern.id = '1'
        self.config_pattern.name = self.__class__.__name__
        print('Name:', self.config_pattern.name)
        self.config_pattern.vars = [x for x, y in self.__dict__.items() if type(y) != FunctionType]
        print('Vars:', self.config_pattern.vars)
        self.config_pattern.properties.parents = [x.__name__ for x in self.__class__.mro() if x != self.__class__ and x != object]
        print('Parents:', self.config_pattern.properties.parents)
        self.config_pattern.properties.children = self.__class__.__subclasses__()
        print('Children:', self.config_pattern.properties.children)
        self.config_pattern.methods.static_methods = [x for x, y in self.__class__.__dict__.items() if type(y) == FunctionType]
        print('Methods:', self.config_pattern.methods.static_methods)

    def parse(self, args):
        return True
