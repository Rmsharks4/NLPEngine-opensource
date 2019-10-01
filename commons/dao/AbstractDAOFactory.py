
import abc
from commons.dao.SparkDAOImpl import SparkDAOImpl


class AbstractDAOFactory(metaclass=abc.ABCMeta):

    @classmethod
    def get_dao(cls, dao_type):
        switcher = {
            SparkDAOImpl.__name__: SparkDAOImpl()
        }
        return switcher.get(dao_type, '')
