from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

class Reaction:
    val = ["Gas", "Solid", "Liquid"]
    R = {"R": [], "P": []}
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1000x200")
        self.win.title("Reaction")
        self.Reaction = Label(self.win, text=" Здесь появится реакция ",font=tkFont.Font(size=22))
        self.Reaction.pack()
        self.b1 = Button(self.win, text="Добавить реагент", command=lambda: self.add_compound("R"), width=20, height=5,font=tkFont.Font(size=16))
        self.b2 = Button(self.win, text="Добавить продукт", command=lambda: self.add_compound("P"), width=20, height=5,font=tkFont.Font(size=16))
        self.b3 = Button(self.win, text="Изменение/удаление", command=self.edit, width=20, height=5)
        self.b1.pack(side=LEFT)
        self.b2.pack(side=RIGHT)
        self.run()

    def edit(self):
        pass

    def add_compound(self, tp):
        adr = Toplevel(self.win)
        adr.geometry("400x100")
        adr.title("Добавить")
        adr.grab_set()
        eadr = Entry(adr, width=20)
        eadr.pack(fill=X)
        com = ttk.Combobox(adr, values=self.val, state="readonly")
        com.current(0)
        com.pack()
        Button(adr, text="Добавить", command=lambda: self.add(False, adr, eadr, com, tp)).pack(fill=BOTH, expand=True)
        Button(adr, text="Добавить ещё", command=lambda: self.add(True, adr, eadr, com, tp)).pack(fill=BOTH, expand=True)


    def add(self, more: bool, adr, e, com, rtype):
        try:
            if e.get() != "":
                if any(letter.isupper() for letter in e.get()):
                    self.R[rtype].append((e.get(), com.get()))
                    adr.destroy()
                    self.change_reaction()
                else:
                    raise Err("Неверный формат ввода!")
            else:
                raise Err("Пустое поле для вещества")
        except Err:
            pass
        else:
            if more:
                self.add_compound(rtype)

    def change_reaction(self):
        answ = str()
        for i in range(len(self.R["R"])):
            answ += self.R["R"][i][0] + "(" + self.R["R"][i][1]+")" + " + "
        answ = answ[0: len(answ)-2]
        answ += " = "
        for i in range(len(self.R["P"])):
            answ += self.R["P"][i][0] + "(" + self.R["P"][i][1]+")" + " + "
        answ = answ[0: len(answ) - 2]
        self.Reaction.config(text=answ)

    def run(self):
        self.win.mainloop()

    def err(self, *args):
        er = Toplevel(self.win)
        er.title("Ошибка")
        Label(er, text="ОШИБКА!").pack(fill=BOTH, expand=True)
        if args:
            Label(er, text=str(args)).pack(fill=BOTH, expand=True)
        Button(er, text="OK", command=lambda: er.destroy()).pack(fill=BOTH, expand=True)


class Err(ValueError):
    def __init__(self, *args):
        ValueError.__init__(self, args)
        er = Tk()
        er.title("Ошибка")
        Label(er, text="ОШИБКА!").pack(fill=BOTH, expand=True)
        if args:
            Label(er, text=str(args[0])).pack(fill=BOTH, expand=True)
        Button(er, text="OK", command=lambda: er.destroy()).pack(fill=BOTH, expand=True)

