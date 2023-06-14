
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from solve import *
import time as t

class Data:

    def __init__(self,d,num):
        self.root=Tk()
        self.a = d
        self.s = solve(num)
        self.mainwin_formation(self.root)
        self.run()

    def mainwin_formation(self, a):
        l = Label(a, text="Проводим базовые рассчеты")
        l.pack()
        l.destroy()
    def run(self):
        self.root.mainloop()