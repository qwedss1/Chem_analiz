from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class Reaction:
    val = ["Gas", "Solid", "Liquid"]
    R = {"R": [], "P": []}

    def __init__(self):
        self.win = Tk()
        self.win.geometry("1000x200")
        self.win.maxsize(1200, 200)
        self.win.title("Reaction")
        self.Reaction = Label(self.win, text=" Здесь появится реакция ", font=tkFont.Font(size=22))
        self.Reaction.pack()
        b1 = Button(self.win, text="Добавить реагент", command=lambda: self.add_compound("R"), width=20, height=5, font=tkFont.Font(size=16))
        b2 = Button(self.win, text="Добавить продукт", command=lambda: self.add_compound("P"), width=20, height=5, font=tkFont.Font(size=16))
        b3 = Button(self.win, text="Изменение/удаление", command=self.edit, width=20, height=5)
        b1.pack(side=LEFT)
        b2.pack(side=RIGHT)
        b3.pack(side=BOTTOM)
        self.run()

    def edit(self):
        ed = Toplevel(self.win)
        ed.geometry("400x100")
        ed.title("Изменить")
        ed.grab_set()
        Label(ed, text="Выберите соединение").grid(row=0, column=0)
        com = ttk.Combobox(ed, values=self.special_edit_formation(self.R), width=20, state="readonly")
        com.grid(row=1, column=0)
        Button(ed, text="Изменить", font=tkFont.Font(size=16), command=lambda: self.edit_(com.get(), ed , com)).grid(row=1, column=1)
        Button(ed, text="Удалить", font=tkFont.Font(size=16), command=lambda: self.del_func(com.get(), ed, com)).grid(row=2, column=1)

    def edit_(self, c, root, com):
        self.del_func(c, root, com)
        self.add_compound(c[0])


    def del_func(self, c, root, com):
        keyw="R"
        if c[0] == "R":
            pass
        else:
            keyw="P"
        my_edition=self.R[keyw]
        for x in my_edition:
            if x[0]==c[2:]:
                my_edition.remove(x)
        self.R[keyw]=my_edition
        self.change_reaction()
        com.config(values=self.special_edit_formation(self.R))
        root.destroy()

    def special_edit_formation(self,r):
        answ = []
        re = r["R"]
        pr = r["P"]
        for x in re:
            str = "R:"
            str += x[0]
            answ.append(str)
        for x in pr:
            str = "P:"
            str += x[0]
            answ.append(str)
        return answ

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
