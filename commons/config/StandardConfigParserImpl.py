"""
    Created By: Ramsha Siddiqui
    Description: This is an implementation of the Abstract Config Parser Class -
    we implement the configurations of Pre-Processing in this one ...
"""

from commons.config.AbstractConfigParser import AbstractConfigParser
from commons.config.AbstractConfig import AbstractConfig
from types import FunctionType


class StandardConfigParserImpl(AbstractConfigParser):

    def __init__(self):
        super().__init__()

    def init_config(self):
        self.config_pattern.id = hash(self.__class__.__name__)
        self.config_pattern.name = self.__class__.__name__
        self.config_pattern.vars = [x for x, y in self.__dict__.items() if type(y) != FunctionType]
        self.config_pattern.properties.parents = [x.__name__ for x in self.__class__.mro() if x != self.__class__ and x != object]
        self.config_pattern.properties.children = self.__class__.__subclasses__()
        self.config_pattern.methods.static_methods = [x for x, y in self.__class__.__dict__.items()
                                                      if type(y) == FunctionType]
        self.config_pattern.properties = self.config_pattern.properties.__dict__
        self.config_pattern.methods = self.config_pattern.methods.__dict__

    def parse(self):
        self.init_config()
        self.read({
            AbstractConfig.__name__: self.config_pattern.__dict__
        })
        self.write(self.__class__.__name__+'.ini')
