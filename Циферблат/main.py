# [<B>] Подключение библиотек
from fltk import *
from circle import Generator
from window import Window

# [<G>] Глобальные переменные
# Спираль:
_H = 600  # - Высота окна
_W = 800  # - Ширина окна
_r = 200  # - радиус окружности
_t = 12  # - точек на окружности
tick = 0.00
_sec = -1
_min = -1
_boxSizes = (40, 40)  # - размер кнопки (по умолчанию)
buttons_hours = []  # - список кнопок спирали
label_rome = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII']
MainWindow = Window(20, 180, _W, _H, 'Циферблат')  # Экземпляр окна спирали


# [<F>] Основные функции
# Создание и обновление спирали
def generate_btns():
    # вычисляем координаты начальной точки спирали
    _X1 = (_W / 2) - _boxSizes[0]
    _Y1 = (_H / 2) - _boxSizes[1]

    # вычисляем точки
    gen_secs = Generator(_r, _t, _X1, _Y1)

    # Создаем и добавляем кнопки в список
    gen_secs.generate_crds()
    coos = gen_secs.getXYList()
    for item in coos:
        # указываем позиции, размеры и текст кнопок
        _btn = Fl_Box(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
        _btn.label(str(coos.index(item) + 1))
        _btn.box(FL_ROUND_UP_BOX)
        buttons_hours.append(_btn)


def init_interface():
    for item in buttons_hours:
        MainWindow.add(item)

    MainWindow.begin()
    _l_button = Fl_Light_Button(5, 5, 110, 30, 'Arabic / Rome')
    _l_button.callback(number_cb)
    MainWindow.end()


# [<C>] Обработка событий
def number_cb(fl_obj):
    if fl_obj.value() == 1:
        i = 0
        for item in buttons_hours:
            item.label(str(label_rome[i]))
            i += 1
    else:
        for item in buttons_hours:
            item.label(str(buttons_hours.index(item)))
# [</C>]


# [!] Точка входа в программу
def main():
    generate_btns()  # генерация спирали из кнопок

    init_interface()

    # Запуск графической оболочки
    Fl.run()


# [->] Вызов точки входа
if __name__ == "__main__":
    main()
# [<-]
