# Переопределение класса (конструктора класса) Fl_Window
# Упрощает код создания экзепляра окна

from fltk import *

class Window(Fl_Window):

    # Конструктор
    def __init__(self, x, y, w, h, label): #x,y,w,h,l     w,h,l
        Fl_Window.__init__(self, x, y, w, h, label)
        self.end()
        self.show()

