from tkinter import *
import tkinter.font as tkFont
from solve import *
from reaction import Err


class Data:

    def __init__(self,d,num):
        self.Init = d
        self.num=num
        self.s = solve(num)
        self.mainwin()
        self.run()

    def mainwin(self):
        self.root=Tk()
        fs = 20
        root = self.root
        root.geometry("800x600")
        root.minsize(800, 600)
        root.maxsize(800, 600)
        root.title("Информация")
        root.iconbitmap("icon.ico")
        root.configure(background="gray")
        Label(root, height=2, background="gray").pack()
        Label(root, text=self.s.reaction, font=tkFont.Font(size=28), justify="center").pack()
        Label(root, height=2, background="gray").pack()
        Label(root, text=f"T={int(self.s.temp)} K", justify="center", font=tkFont.Font(size=fs), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fs)).pack()
        Label(root, text=f"dHT={round(self.s.dH*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fs), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fs)).pack()
        Label(root, text=f"dGT={round(self.s.dG*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fs), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fs)).pack()
        Label(root, text=f"dST={round(self.s.dS*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fs), width=25).pack()
        Label(root, height=1, background="gray").pack()
        Button(text="Изменить температуру", command=self.change_T, font=tkFont.Font(size=fs-2), width=25, height=1, justify="center").pack()
        Button(text="Дополнительный рассчет", command=self.additional, font=tkFont.Font(size=fs-2), width=25, height=1, justify="center").pack()
        Button(text="Меню", command=self.Menu, font=tkFont.Font(size=fs-2), width=25, height=1, justify="center").pack()
        Button(text="Выход", command=lambda: root.destroy(), font=tkFont.Font(size=fs-2), width=25, height=1, justify="center").pack()

    def change_T(self):
        with open(f"Reactions/Reaction{self.num}/React.json","r") as f:
            self.R=json.load(f)
        ad = Toplevel(self.root)
        w,h=300,100
        ad.geometry(str(w)+"x"+str(h))
        ad.minsize(w,h)
        ad.maxsize(w,h)
        ad.title("Изменение температуры")
        ad.grab_set()
        Label(ad, text=f"Текущая температура=> {self.s.temp}", font=tkFont.Font(size=20), justify="center").pack()
        Label(ad, text="Введите новую температуру:", font=tkFont.Font(size=20), justify="center").pack()
        e=Entry(ad, font=tkFont.Font(size=20), justify="center")
        e.pack(fill=X)
        var = StringVar(value="K")
        Radiobutton(ad, text="K", variable=var, value="K").pack(side=LEFT)
        Radiobutton(ad, text="C", variable=var, value="C").pack(side=LEFT)
        Button(ad, text="Применить", command=lambda: self.changing(e, var, ad)).pack()

    def changing(self, e, var, ad):
        try:
            if e.get() == "" or not e.get().isnumeric():
                raise Err("Неверная температура!")
            else:
                if var.get() == "K":
                    self.R["T"] = float(e.get())
                else:
                    self.R["T"] = float(e.get()) + 273
                if not self.check(self.R):
                    raise Err("Температура не поддерживается", self.root)
                else:
                    if os.path.exists("Reactions"):
                        pass
                    else:
                        os.mkdir("Reactions")
                    a = "Reactions/Reaction" + self.num
                    os.mkdir(a)
                    a += "/" + "React.json"
                    with open(a, "w") as f:
                        json.dump(self.R, f)
                    ad.destroy()
                    self.root.destroy()
                    self.__init__(self.Init, self.num)
        except Err:
            pass

    def check(self, R):
        state = True
        conn = sq.connect('db.db')
        cur = conn.cursor()
        for n in range(0, len(R["R"])):
            a = "SELECT Tmax FROM therdb WHERE formula='" + str(R["R"][n][0]) + "'"
            cur.execute(a)
            b = int(cur.fetchone()[0])
            if b < R["T"]:
                state = False
                break
        for n in range(0, len(R["P"])):
            a = "SELECT Tmax FROM therdb WHERE formula='" + str(R["P"][n][0]) + "'"
            cur.execute(a)
            b = int(cur.fetchone()[0])
            if b < R["T"]:
                state = False
                break
        return state

    def additional(self):
        self.root.destroy()
        self.Init.moredata(self.num)
        self.del_me()

    def Menu(self):
        self.root.destroy()
        self.Init.menu()
        self.del_me()

    def del_me(self):
        del self

    def run(self):
        self.root.mainloop()