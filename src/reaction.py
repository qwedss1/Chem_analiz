from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import json
import os


class Reaction:
    val = ["Gas", "Solid", "Liquid"]
    R = {"R": [], "P": []}

    def __init__(self):
        self.win = Tk()
        self.win.geometry("1000x220")
        self.win.maxsize(1200, 220)
        self.win.minsize(800, 220)
        self.win.title("Reaction")
        self.Reaction = Label(self.win, text=" Здесь появится реакция ", font=tkFont.Font(size=22))
        self.Reaction.pack()
        b1 = Button(self.win, text="Добавить реагент", command=lambda: self.add_compound("R"), width=15, height=2, font=tkFont.Font(size=16))
        b2 = Button(self.win, text="Добавить продукт", command=lambda: self.add_compound("P"), width=15, height=2, font=tkFont.Font(size=16))
        b3 = Button(self.win, text="Изменение/удаление", command=self.edit, width=20, height=2, font=tkFont.Font(size=16))
        b4 = Button(self.win, text="Рассчёт", width=20, height=2, command=self.readyness, font=tkFont.Font(size=16))
        b1.pack(side=LEFT)
        b2.pack(side=RIGHT)
        b3.pack(side=BOTTOM)
        b4.pack(side=BOTTOM)
        self.run()

    def readyness(self):
        try:
            if self.Reaction.cget("text") != "" and self.Reaction.cget("text") != " Здесь появится реакция ":
                if self.R["R"] != [] and self.R["P"] != []:
                    end = Toplevel(self.win)
                    end.grab_set()
                    end.geometry("300x100")
                    end.title("Ввод окончен")
                    Label(end, text="Введите температуру", font=tkFont.Font(size=16)).pack()
                    e = Entry(end)
                    e.pack()
                    var = StringVar(value="K")
                    Radiobutton(end, text="K", variable=var, value="K").pack(side=LEFT)
                    Radiobutton(end, text="C", variable=var, value="C").pack(side=LEFT)
                    Button(end, text="OK", font=tkFont.Font(size=16), command=lambda: self.save_info_and_die(e, var)).pack(side=BOTTOM)
                else:
                    raise Err("Мало данных!", self.win)
            else:
                raise Err("Поле ввода реакции пустое!", self.win)
        except Err:
            pass

    def save_info_and_die(self, e, var):
        try:
            if e.get() == "" or not e.get().isnumeric():
                raise Err("Неверная температура!")
            else:
                if var.get() == "K":
                    self.R["T"] = float(e.get())
                else:
                    self.R["T"] = float(e.get()) + 273
                if os.path.exists("Reactions"):
                    pass
                else:
                    os.mkdir("Reactions")
                a = "Reactions/Reaction" + self.get_num_reaction()
                os.mkdir(a)
                a += "/" + "React.json"
                with open(a, "a") as f:
                    json.dump(self.R, f)
                self.win.destroy()
        except Err:
            pass

    def is_latin(self,text):
        for char in text:
            if not char.isalnum() or ord(char) > 127:
                return False
        return True

    def get_num_reaction(self):
        folder = "Reactions"
        files = os.listdir(folder)
        try:
            for x in files:
                if "Reaction" not in x:
                    raise Err("В папке с реакциями завелась нечисть")
        except:
            pass
        else:
            d = [0]
            for x in files:
                d.append(int(x[8:]))
            return str(max(d)+1)

    def edit(self):
        ed = Toplevel(self.win)
        ed.geometry("400x100")
        ed.title("Изменить")
        ed.grab_set()
        Label(ed, text="Выберите соединение").grid(row=0, column=0)
        com = ttk.Combobox(ed, values=self.special_edit_formation(self.R), width=20, state="readonly")
        com.grid(row=1, column=0)
        Button(ed, text="Изменить", font=tkFont.Font(size=16), command=lambda: self.edit_(com.get(), ed, com)).grid(row=1, column=1)
        Button(ed, text="Удалить", font=tkFont.Font(size=16), command=lambda: self.del_func(com.get(), ed, com)).grid(row=2, column=1)

    def edit_(self, c, root, com):
        self.del_func(c, root, com)
        self.add_compound(c[0])

    def del_func(self, c, root, com):
        keyw = "R"
        if c[0] == "R":
            pass
        else:
            keyw = "P"
        my_edition = self.R[keyw]
        for x in my_edition:
            if x[0] == c[2:]:
                my_edition.remove(x)
        self.R[keyw] = my_edition
        self.change_reaction()
        com.config(values=self.special_edit_formation(self.R))
        root.destroy()

    def special_edit_formation(self, r):
        answ = []
        re = r["R"]
        pr = r["P"]
        for x in re:
            st = "R:"
            st += x[0]
            answ.append(st)
        for x in pr:
            st = "P:"
            st += x[0]
            answ.append(st)
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
                if any(letter.isupper() for letter in e.get()) and self.is_latin(e.get()) and e.get()[0].isupper():
                    self.R[rtype].append((e.get(), com.get()))
                    adr.destroy()
                    self.change_reaction()
                else:
                    raise Err("Неверный формат ввода!", self.win)
            else:
                raise Err("Пустое поле для вещества", self.win)
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


class Err(ValueError):
    def __init__(self, *args):
        ValueError.__init__(self, args)
        er = Toplevel(args[1])
        er.title("Ошибка")
        er.grab_set()
        Label(er, text="ОШИБКА!").pack(fill=BOTH, expand=True)
        if args:
            Label(er, text=str(args[0])).pack(fill=BOTH, expand=True)
        Button(er, text="OK", command=lambda: er.destroy()).pack(fill=BOTH, expand=True)
