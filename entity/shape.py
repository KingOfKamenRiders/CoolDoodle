from enum import Enum


class Shape(Enum):
    TRIANGLE = 1
    RECTANGLE = 2
    CIRCLE = 3

    def __str__(self):
        if self == Shape.TRIANGLE:
            return '三角形'
        elif self == Shape.RECTANGLE:
            return '正方形'
        elif self == Shape.CIRCLE:
            return '圆型'
        else:
            return 'unknown'
