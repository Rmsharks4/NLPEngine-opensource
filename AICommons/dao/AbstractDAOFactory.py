
import abc
from commons.dao.PandasDAOImpl import PandasDAOImpl


class AbstractDAOFactory(metaclass=abc.ABCMeta):

    @classmethod
    def get_dao(cls, dao_type):
        switcher = {
            PandasDAOImpl.__name__: PandasDAOImpl()
        }
        return switcher.get(dao_type, '')
