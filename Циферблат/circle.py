# Класс генератора координат

from fltk import *
import math


class Generator:
    __listXY = []  # cписок координат

    # Конструктор (параметры: расстояние, шаг, точки начала)
    def __init__(self, r, t, x, y):
        self.__r = r
        self.__t = t
        self.__x = x
        self.__y = y

    # Получение списка коорданит из класса
    def getXYList(self):
        return self.__listXY

    # Функция вычисления координат спирали
    def generate_crds(self):
        step = math.radians(360 / self.__t) * (self.__t / -4) + math.radians(360 / self.__t)
        _i = 0
        if len(self.__listXY) > 0:
            self.__listXY.clear()

        while _i < self.__t:
            x = self.__x + self.__r * math.cos(step)
            y = self.__y + self.__r * math.sin(step)
            self.__listXY.append((math.ceil(x), math.ceil(y)))
            step += math.radians(360 / self.__t)
            _i += 1
