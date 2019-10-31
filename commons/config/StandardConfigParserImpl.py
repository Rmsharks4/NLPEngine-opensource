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
        childlist = [x() for x in self.__class__.__subclasses__()]
        check = True
        while check:
            notchilds = []
            for child in childlist:
                if len(child.__class__.__subclasses__()) > 0:
                    notchilds.append(child)
                    check = True
            if len(notchilds) == 0:
                check = False
            for child in notchilds:
                childlist.remove(child)
                for x in child.__class__.__subclasses__():
                    childlist.append(x())
        self.config_pattern.properties.children = [x.__class__.__name__ for x in childlist]
        self.config_pattern.methods.static_methods = [x for x, y in self.__class__.__dict__.items()
                                                      if type(y) == FunctionType]

    def reformat_config(self):
        self.config_pattern.properties = self.config_pattern.properties.__dict__
        self.config_pattern.methods = self.config_pattern.methods.__dict__

    def parse(self):
        self.init_config()
        self.reformat_config()
        self.read_dict({
            AbstractConfig.__name__: self.config_pattern.__dict__
        })
        self.write(self.__class__.__name__+'.ini')
