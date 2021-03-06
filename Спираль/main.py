# [<B>] Подключение библиотек
from fltk import *
from spiral import Generator as Gen


# Переопределение класса (конструктора класса) Fl_Window
# Упрощает код создания экзепляра окна
class Window(Fl_Window):
    # Конструктор
    def __init__(self, x, y, w, h, label):  # x,y,w,h,l
        Fl_Window.__init__(self, x, y, w, h, label)
        self.end()
        self.show()


# [<G>] Глобальные переменные
# Спираль:
_H = 600  # - Высота окна
_W = 800  # - Ширина окна
_h = 12  # - расстояние между витками
_t = 0.8  # - шаг по спирали

_boxSizes = (1, 1)  # - размер кнопки (по умолчанию)
buttons = []  # - список кнопок спирали
alpha = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # алфавит для кнопок спирали

SpiralWindow = Window(20, 180, _W, _H, 'Спираль')  # Экземпляр окна спирали


# [<F>] Основные функции
# Создание и обновление спирали
def generate_btns():
    # вычисляем координаты начальной точки спирали
    _X1 = (_W / 2) - _boxSizes[0]
    _Y1 = (_H / 2) - _boxSizes[1]

    # вычисляем точки
    gen = Gen(_h, _t, _X1, _Y1)
    gen.GenerateCoos()

    # Создаем и добавляем кнопки в список
    char = 0
    for item in gen.GetXYList():
        # указываем позиции, размеры и текст кнопок
        _btn = Fl_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], alpha[char])
        _btn.box(FL_NO_BOX)
        buttons.append(_btn)
        char += 1


# [!] Точка входа в программу
def main():
    generate_btns()  # генерация спирали из кнопок

    # добавляем кнопки в окно Спирали
    for item in buttons:
        SpiralWindow.add(item)

    # Запуск графической оболочки
    Fl.run()


# [->] Вызов точки входа
if __name__ == "__main__":
    main()
# [<-]
