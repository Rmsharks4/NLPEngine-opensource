
import abc
from commons.dao.ConfigDAOImpl import ConfigDAOImpl
from commons.dao.SparkDAOImpl import SparkDAOImpl


class AbstractDAOFactory(metaclass=abc.ABCMeta):

    @classmethod
    def get_dao(cls, dao_type):
        switcher = {
            SparkDAOImpl.__name__: SparkDAOImpl(),
            ConfigDAOImpl.__name__: ConfigDAOImpl()
        }
        return switcher.get(dao_type, '')
