# [<B>] Подключение библиотек
from fltk import *
from spiral import Generator
from window import Window
from sys import *


# [<G>] Глобальные переменные
# Спираль:
_H = 600  # - Высота окна
_W = 800  # - Ширина окна
_r = 160  # - радиус окружности
_t = 60  # - точек на окружности
tick = 0
_boxSizes = (20, 20)  # - размер кнопки (по умолчанию)
buttons_secs = []  # - список кнопок спирали
buttons_mins = []
MainWindow = Window(20, 180, _W, _H, 'Секундомер')  # Экземпляр окна спирали


# [<F>] Основные функции
# Создание и обновление спирали
def generate_btns():
    # вычисляем координаты начальной точки спирали
    _X1 = (_W / 2) - _boxSizes[0]
    _Y1 = (_H / 2) - _boxSizes[1]

    # вычисляем точки
    gen_secs = Generator(_r, _t, _X1, _Y1)
    gen_mins = Generator(_r + 40, _t, _X1, _Y1)

    # Создаем и добавляем кнопки в список
    gen_secs.GenerateCoos()
    for item in gen_secs.GetXYList():
        # указываем позиции, размеры и текст кнопок
        _btn = Fl_Radio_Round_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
        buttons_secs.append(_btn)

    gen_mins.GenerateCoos()
    for item in gen_mins.GetXYList():
        # указываем позиции, размеры и текст кнопок
        _btn1 = Fl_Radio_Round_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
        buttons_mins.append(_btn1)


# [<C>] Обработка событий
def timer_cb():
    global _t, tick

    if tick > 0:
        buttons_secs[(tick-1) % 60].value(0)

    buttons_secs[tick % 60].value(1)
    print('Time is {0}'.format(tick))
    tick += 0.01
    Fl.repeat_timeout(0.01, timer_cb)


# [!] Точка входа в программу
def main():
    generate_btns()  # генерация спирали из кнопок

    # добавляем кнопки в окно Спирали
    for item1 in buttons_mins:
        MainWindow.add(item1)
    for item in buttons_secs:
        MainWindow.add(item)
    Fl.add_timeout(1.0, timer_cb)

    # Запуск графической оболочки
    Fl.run()


# [->] Вызов точки входа
if __name__ == "__main__":
    main()
# [<-]
