"""
    Created By: Ramsha Siddiqui
    Description: This is a class for Abstract COnfiguration Properties (Parent and CHild CLasses, as well as Dependant Data)
"""

class AbstractConfigProperties:

    def __init__(self):
        self.cls_req_args = list()
        self.cls_req_data = list()
        self.cls_parents = list()
        self.cls_children = list()

    @property
    def req_args(self):
        return self.cls_req_args

    @req_args.setter
    def req_args(self, args):
        self.cls_req_args = args

    @property
    def req_data(self):
        return self.cls_req_data

    @req_data.setter
    def req_data(self, args):
        self.cls_req_data = args

    @property
    def parents(self):
        return self.cls_parents

    @parents.setter
    def parents(self, args):
        self.cls_parents = args

    @property
    def children(self):
        return self.cls_children

    @children.setter
    def children(self, args):
        self.cls_children = args
