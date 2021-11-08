# [<B>] Подключение библиотек
from fltk import *
from spiral import Generator as Gen
from window import Window

# [<G>] Глобальные переменные
# Спираль:
_H = 400  # - Высота окна
_W = 600  # - Ширина окна
_h = 40  # - расстояние между витками
_t = 0.3  # - шаг по спирали
_boxSizes = (15, 15)  # - размер кнопки (по умолчанию)
buttons = []  # - список кнопок спирали
alpha = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"  # алфавит для кнопок спирали

MainWindow = Window(20, 40, 250, 90, 'Параметры')  # Экземпляр главного окна
SpiralWindow = Window(20, 180, _W, _H, 'Спираль')  # Экземпляр окна спирали


# [<F>] Основные функции
# Создание и обновление спирали
def generate_buttons():
    # вычисляем координаты начальной точки спирали
    _X1 = (_W / 2) - _boxSizes[0]
    _Y1 = (_H / 2) - _boxSizes[1]

    # вычисляем точки
    gen = Gen(_h, _t, _X1, _Y1)
    gen.calculate_xy()

    if len(buttons) > 0:
        buttons.clear()
        SpiralWindow.clear()
    # Создаем и добавляем кнопки в список
    char = 0
    for item in gen.get_xy_list():
        # указываем позиции, размеры и текст кнопок
        _btn = Fl_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], alpha[char % 33])
        # _btn.box(FL_NO_BOX)
        buttons.append(_btn)
        char += 1

    # добавляем кнопки в окно Спирали
    for item in buttons:
        SpiralWindow.add(item)


# Добавление элементов на главное окно
def init_main_window():
    MainWindow.begin()  # точка начала перечисления элементов

    # [!] Создаем поле ввода для действительных чисел
    t_input = Fl_Float_Input(20, 15, 60, 25, 't')  # создаем элемент указав размеры, позицию и подпись
    t_input.labelfont(FL_ITALIC)  # формат шрифта подписи
    t_input.value(str(_t))  # первоначальное значение
    t_input.callback(th_input_cb, 't')  # определяем функцию-обработчик изменения значения поля и имя изменяемого значения
    t_input.when(FL_WHEN_CHANGED)  # указываем когда нужно обработать события (как только измениться значение в поле)

    h_input = Fl_Int_Input(20, 50, 60, 25, 'h')
    h_input.labelfont(FL_ITALIC)
    h_input.value(str(_h))
    h_input.callback(th_input_cb, 'h')
    h_input.when(FL_WHEN_CHANGED)

    x_input = Fl_Int_Input(170, 15, 60, 25, 'Ширина')
    x_input.labelfont(FL_ITALIC)
    x_input.value(str(_W))
    x_input.callback(xy_input_cb, 'x')
    x_input.when(FL_WHEN_CHANGED)

    y_input = Fl_Int_Input(170, 50, 60, 25, 'Высота')
    y_input.labelfont(FL_ITALIC)
    y_input.value(str(_H))
    y_input.callback(xy_input_cb, 'y')
    y_input.when(FL_WHEN_CHANGED)

    MainWindow.end()


# Проверка на ввод действительного числа
def isFloat(val):
    try:
        if float(val) > 0:
            return True
        else:
            return False
    except ValueError:
        # print ('not a number')
        return False


# [<C>] Обработка событий
# Обработка изменения шага и расстояния по спирали
def th_input_cb(fl_obj, val):
    global _t, _h
    o = fl_obj.value()
    if (isFloat(str(o))):
        if val == 't':
            _t = float(o)
        elif val == 'h':
            _h = float(o)
        generate_buttons()
        SpiralWindow.redraw()


# Обработка изменения размеров окна спирали
def xy_input_cb(fl_obj, val):
    global _H, _W
    o = fl_obj.value()
    if (isFloat(o)):
        if val == 'x':
            _W = int(o)
        elif val == 'y':
            _H = int(o)
        SpiralWindow.resize(SpiralWindow.x(), SpiralWindow.y(), _W, _H)
        generate_buttons()
        SpiralWindow.redraw()


# [!] Точка входа в программу
def main():
    init_main_window()  # вызов функции добавлюйщей элементы на главное окно
    generate_buttons()  # генерация спирали из кнопок

    # Запуск графической оболочки
    Fl.run()


# [->] Вызов точки входа
if __name__ == "__main__":
    main()
# [<-]
