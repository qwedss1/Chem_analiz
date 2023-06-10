from tkinter import *
from tkinter import ttk

class Reaction:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("500x200")
        self.win.title("Reaction")
        self.R = {"Reaction": " = ", "R": [], "P": []}
        self.Reaction = Label(self.win, text=self.R["Reaction"])
        self.Reaction.pack()
        self.b1 = Button(self.win, text="Добавить реагент", command=self.addr, width=20, height=5)
        self.b2 = Button(self.win, text="Добавить продукт", command=self.addp, width=20, height=5)
        self.b3 = Button(self.win, text="Изменение/удаление", command=self.edit, width=20, height=5)
        self.b1.pack(side=LEFT)
        self.b2.pack(side=RIGHT)

    def edit(self):
        pass

    def addr(self):
        adr = Toplevel(self.win)
        adr.geometry("400x200")
        adr.title("AddR")
        ladr = Entry(adr, width=20)
        ladr.pack()
        com=ttk.Combobox(vals=)

    def addp(self):
        self.adp = Toplevel(self.win)
        self.adp.geometry("400x200")
        self.adp.title("AddP")

    def change_reaction(self, val):
        self.Reaction.config(text=val)

    def destr(a):
        a.destroy()

    def run(self):
        self.win.mainloop()


p = Reaction()

p.run()
