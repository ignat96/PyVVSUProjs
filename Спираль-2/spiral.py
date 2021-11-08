# Класс генератора координат

from fltk import *
import math

class Generator:

    __listXY = []       # cписок координат
    __spLength = 33     # длинна списка (константа)

    # Конструктор (параметры: расстояние, шаг, точки начала)
    def __init__(self, h, t, x, y):
        self.__h = h
        self.__t = t
        self.__x = x
        self.__y = y

    # Получение списка коорданит из класса
    def get_xy_list(self):
        return self.__listXY

    # Функция вычисления координат спирали
    def calculate_xy(self):
        k = self.__h/(2*math.pi)
        _i = 0
        fstep = 4 * (2*math.pi)
        if len(self.__listXY) > 0:
            self.__listXY.clear()

        while _i < fstep:
            p = k * _i
            x = p * math.cos(_i)
            y = p * math.sin(_i)
            self.__listXY.append((math.ceil(x+self.__x), math.ceil(y+self.__y)))
            _i += self.__t
    