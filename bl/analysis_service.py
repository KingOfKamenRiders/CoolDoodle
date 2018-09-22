from entity.shape import Shape
import numpy as np
import cv2
from abc import ABCMeta,abstractmethod


class AnalyzeService(metaclass=ABCMeta):

    @abstractmethod
    def analyze_shape(self, doodle):
        """
            :param doodle:一个Doodle类对象
            :return: 一个Shape类对象，Shape类是一个枚举类
        """
        pass


class AnalyzeServiceIMP(AnalyzeService):

    def analyze_shape(self, doodle):
        data = []
        for line in doodle.lines:
            i = 0
            while i < len(line):
                data.append([line[i],line[i+1]])
                i = i + 2
        n = cv2.approxPolyDP(np.array(data),.03*cv2.arcLength(np.array(data),True), True)
        print(len(n))
        if len(n) == 3:
            return Shape.TRIANGLE
        elif len(n) == 4:
            return Shape.RECTANGLE
        else:
            return Shape.CIRCLE