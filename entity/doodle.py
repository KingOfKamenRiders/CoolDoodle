from entity.shape import Shape


class Doodle:
    """
    该类是代表一次涂鸦的实体类
    """
    def __init__(self, did=0,shape='', tag='', lines=None):
        if lines is None:
            self._lines = []
        else:
            self._lines = lines
        self._shape = shape
        self._tag = tag
        self._id = did

    @property
    def id(self):
        """
        一次涂鸦的标识符
        :return:
        """
        return self._id

    @property
    def shape(self):
        """
        改涂鸦的形状,由自动识别得来
        :return:
        """
        return self._shape

    @shape.setter
    def shape(self, value):
        if not isinstance(value,Shape):
            raise ValueError('attribute shape must be a Shape!')
        self._shape = value

    @property
    def lines(self):
        """
        该涂鸦的点集,是一个二维数组, 第一维是线, 第二维是首尾相连的(x,y)的点坐标
        :return:
        """
        return self._lines

    @lines.setter
    def lines(self, value):
        if not isinstance(value, list) :
            raise ValueError('attribute lines must be a 2-d list!')
        self._lines = value

    @property
    def tag(self):
        """
        用户为该次涂鸦打的tag, 是一个字符串
        :return:
        """
        return self._tag

    @tag.setter
    def tag(self, value):
        if not isinstance(value,str):
            raise ValueError('attribute tag must be a str!')
        self._tag = value
