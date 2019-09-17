"""
    Created By: Ramsha Siddiqui
    Description: This is a class for Abstract COnfiguration Methods (FUnctions - three types)
"""

class AbstractConfigMethods:

    def __init__(self):
        self.cls_static_methods = list()
        self.cls_impl_methods = list()
        self.cls_abs_methods = list()

    @property
    def static_methods(self):
        return self.cls_static_methods

    @static_methods.setter
    def static_methods(self, args):
        self.cls_static_methods = args

    @property
    def impl_methods(self):
        return self.cls_impl_methods

    @impl_methods.setter
    def impl_methods(self, args):
        self.cls_impl_methods = args

    @property
    def abs_methods(self):
        return self.cls_abs_methods

    @abs_methods.setter
    def abs_methods(self, args):
        self.cls_abs_methods = args
