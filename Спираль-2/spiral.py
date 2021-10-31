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
    def GetXYList(self):
        return self.__listXY

    # Функция вычисления координат спирали
    def GenerateCoos(self):
        step = 0
        _i = 0
        if (len(self.__listXY) > 0):
            self.__listXY.clear()

        while (_i < self.__spLength):
            x = self.__x - (self.__h * step * math.sin(step))
            y = self.__y + (self.__h * step * math.cos(step))
            self.__listXY.append((math.ceil(x), math.ceil(y)))
            step += self.__t
            _i += 1
    