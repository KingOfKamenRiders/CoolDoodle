from data.doodle_dao import DoodleDAO
from abc import ABCMeta, abstractmethod


class DoodleService(metaclass=ABCMeta):

    @abstractmethod
    def save_doodle(self, doodle):
        """

        :param doodle:一个需要持久化的Doodle类对象
        :return: 改方法没有返回值
        """
        pass

    @abstractmethod
    def get_doodle(self):
        """
        改方法目前没有参数，未来可考率加入关键字参数
        :return:一个Doodle类对象
        """
        pass


class DoodleServiceIMP(DoodleService):
    def __init__(self):
        self.doodle_dao = DoodleDAO()

    def save_doodle(self, doodle):
        self.doodle_dao.save_doodle(doodle)

    def get_doodle(self):
        return self.doodle_dao.load_doodle()
