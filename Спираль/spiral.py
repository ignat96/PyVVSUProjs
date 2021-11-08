# Класс генератора координат

from fltk import *
import math

class Generator:

    listXY = []       # cписок координат
    __spLength = 33     # длинна списка (константа)

    # Конструктор (параметры: расстояние, шаг, точки начала)
    def __init__(self, h, t, x, y, a):
        self.__h = h
        self.__t = t
        self.__x = x
        self.__y = y
        self.__a = a

    # Функция вычисления координат спирали
    def calculate_xy(self):
        k = self.__h/(2*math.pi)    # перевод в радианную меру расстояния между витками
        _i = 0
        fstep = self.__a * (2*math.pi)  # конечная точка спирали
        if len(self.listXY) > 0:
            self.listXY.clear()

        while _i < fstep:
            p = k * _i              # получаем значения шага спирали
            x = p * math.cos(_i)    # нахождение абсциссы
            y = p * math.sin(_i)    # нахождение ординаты
            self.listXY.append((math.ceil(x+self.__x), math.ceil(y+self.__y)))
            _i += self.__t
    