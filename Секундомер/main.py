# [<B>] Подключение библиотек
from fltk import *
from spiral import Generator
from window import Window

# [<G>] Глобальные переменные
# Спираль:
_H = 600  # - Высота окна
_W = 800  # - Ширина окна
_r = 200  # - радиус окружности
_t = 60  # - точек на окружности
tick = 0.00
_sec = -1
_min = -1
_boxSizes = (20, 20)  # - размер кнопки (по умолчанию)
buttons_secs = []  # - список кнопок спирали
buttons_mins = []
MainWindow = Window(20, 180, _W, _H, 'Секундомер')  # Экземпляр окна спирали
TimeDisplay = Fl_Output(int(_W/2)-50,int(_H/2)-25,80,25)


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
    coos = gen_secs.GetXYList()
    for item in coos:
        # указываем позиции, размеры и текст кнопок
        _btn = Fl_Radio_Round_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
        _btn.align(FL_ALIGN_BOTTOM)
        buttons_secs.append(_btn)

    gen_mins.GenerateCoos()
    coos = gen_mins.GetXYList()
    for item in coos:
        # указываем позиции, размеры и текст кнопок
        _btn1 = Fl_Radio_Round_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
        buttons_mins.append(_btn1)


def init_interface():
    for item in buttons_mins:
        MainWindow.add(item)
    for item in buttons_secs:
        MainWindow.add(item)

    MainWindow.add(TimeDisplay)
    MainWindow.begin()
    btn_start = Fl_Button(int(_W / 2)-85, int(_H / 2) + 20, 50, 25, 'Start')
    btn_start.callback(start_cb)
    btn_stop = Fl_Button(int(_W / 2)-35, int(_H / 2)+20, 50, 25, 'Stop')
    btn_stop.callback(stop_cb)
    btn_reset = Fl_Button(int(_W / 2) + 15, int(_H / 2) + 20, 50, 25, 'Reset')
    btn_reset.callback(reset_cb)
    MainWindow.end()


# [<C>] Обработка событий
def timer_cb():
    global _t, tick, _sec, _min

    if _sec < int(tick):
        _sec = int(tick)
        if _sec > 0:
            buttons_secs[(_sec - 1) % 60].value(0)
        buttons_secs[_sec % 60].value(1)
        if _sec % 60 == 0:
            _min += 1
            if _min > 0:
                buttons_mins[(_min - 1) % 60].value(0)
            buttons_mins[_min % 60].value(1)
    tick += 0.01
    TimeDisplay.value('{0}:{1}:{2}'.format(_min,_sec%60,int(tick*100)%100))
    Fl.repeat_timeout(0.01, timer_cb)


def reset_cb(fl_obj):
    global _sec, _min, tick
    _sec = -1
    _min = -1
    tick = 0.00
    TimeDisplay.value('{0}:{1}:{2}'.format(0,0,0))
    Fl.remove_timeout(timer_cb)


def stop_cb(fl_obj):
    Fl.remove_timeout(timer_cb)


def start_cb(fl_obj):
    Fl.add_timeout(0.01, timer_cb)
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
