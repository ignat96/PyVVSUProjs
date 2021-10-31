# [<B>] Подключение библиотек
from fltk import *
from spiral import Generator as Gen
from window import Window



# [<G>] Глобальные переменные
# Спираль:
_H = 600            # - Высота окна
_W = 800            # - Ширина окна
_r = 180             # - радиус окружности
_t = 60           # - точек на окружности
tick = 0
_boxSizes = (20,20)   # - размер кнопки (по умолчанию)
buttons = []        # - список кнопок спирали

MainWindow = Window(20,180,_W,_H, 'Секундомер')  # Экземпляр окна спирали




# [<F>] Основные функции
# Создание и обновление спирали
def GenerateBtns():

    # вычисляем координаты начальной точки спирали
    _X1 = (_W / 2) - _boxSizes[0]
    _Y1 = (_H / 2) - _boxSizes[1]

    # вычисляем точки
    gen = Gen(_r, _t, _X1, _Y1)
    gen.GenerateCoos()
    # Создаем и добавляем кнопки в список
    if (len(buttons) == 0):
        for item in gen.GetXYList():
            # указываем позиции, размеры и текст кнопок
            _btn = Fl_Radio_Round_Button(item[0], item[1], _boxSizes[0], _boxSizes[1], '')
            # _btn.box(FL_NO_BOX)
            buttons.append(_btn)
    # Если кнопки уже были созданы, то обновляем координаты
    else:
        i = 0
        for item in gen.GetXYList():
            buttons[i].position(item[0], item[1])
            i += 1


# [<C>] Обработка событий


def timer_cb():
    global _t, tick
    
    buttons[tick].value(1)
    print('Time is {0}'.format(tick))
    tick += 1
    Fl.repeat_timeout(1.0,timer_cb)
    




# [!] Точка входа в программу
def main():
    
    GenerateBtns() # генерация спирали из кнопок

    # добавляем кнопки в окно Спирали
    for item in buttons:
        MainWindow.add(item)

    Fl.add_timeout(1.0,timer_cb)

    # Запуск графической оболочки
    Fl.run()
# [->] Вызов точки входа
if __name__ == "__main__":
    main() 
# [<-] 