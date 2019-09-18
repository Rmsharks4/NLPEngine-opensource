"""
    Created By: Ramsha Siddiqui
    Description: This is a class for Abstract COnfiguration Properties (Parent and CHild CLasses, as well as Dependant Data)
"""

class AbstractConfigProperties:

    def __init__(self):
        self.req_args = list()
        self.req_data = list()
        self.parents = list()
        self.children = list()

    @property
    def req_args(self):
        return self.req_args

    @req_args.setter
    def req_args(self, args):
        self.req_args = args

    @property
    def req_data(self):
        return self.req_data

    @req_data.setter
    def req_data(self, args):
        self.req_data = args

    @property
    def parents(self):
        return self.parents

    @parents.setter
    def parents(self, args):
        self.parents = args

    @property
    def children(self):
        return self.children

    @children.setter
    def children(self, args):
        self.children = args
