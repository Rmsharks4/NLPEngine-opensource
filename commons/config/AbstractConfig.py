"""
    Created By: Ramsha Siddiqui
    Description: This is a class for Abstract COnfiguration (what's to be dumped inside a config file)
"""

from commons.config.AbstractConfigProperties import AbstractConfigProperties
from commons.config.AbstractConfigMethods import AbstractConfigMethods


class AbstractConfig:

    def __init__(self):
        self.cls_id = None
        self.cls_name = None
        self.cls_properties = AbstractConfigProperties()
        self.cls_methods = AbstractConfigMethods()
        self.cls_vars = list()

    @property
    def id(self):
        return self.cls_id

    @id.setter
    def id(self, args):
        self.cls_id = args

    @property
    def name(self):
        return self.cls_name

    @name.setter
    def name(self, args):
        self.cls_name = args

    @property
    def properties(self):
        return self.cls_properties

    @properties.setter
    def properties(self, args):
        self.cls_properties = args

    @property
    def vars(self):
        return self.cls_vars

    @vars.setter
    def vars(self, args):
        self.cls_vars = args

    @property
    def methods(self):
        return self.cls_methods

    @methods.setter
    def methods(self, args):
        self.cls_methods = args
