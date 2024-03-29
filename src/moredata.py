from tkinter import *
import tkinter.font as tkFont
import json
from inter_addit import *


class Moredata:
    def __init__(self,a,num, t):
        self.Init=a
        self.T=t
        self.num=num
        self.pathC=f"Reactions/Reaction{num}/Calcu.json"
        self.pathR = f"Reactions/Reaction{num}/React.json"
        self.make_root()
        self.run()

    def make_root(self):
        self.root = Tk()
        root = self.root
        w,h=520,500
        root.geometry(f"{w}x{h}")
        root.minsize(w, h)
        root.maxsize(w, h)
        root.config(bg="gray")
        root.title("Дополнительные рассчеты")
        self.make_menu(root)

    def make_menu(self, root):
        fs=20
        Label(root, text=f"Можно рассчитать:", font=tkFont.Font(size=fs), justify="center").pack(fill=X)
        Label(root, bg="gray").pack()
        if self.is_state() == "L":
            Button(root, text="Энергия активации", font=tkFont.Font(size=fs), command=lambda: self.Engac()).pack(fill=X)
            Button(root, text="Равновесные концентрации", font=tkFont.Font(size=fs), command=lambda: self.ravnl()).pack(fill=X)
        if self.is_state() == "G":
            Button(root, text="Равновесные мольные доли", font=tkFont.Font(size=fs),command=lambda: self.doli()).pack(fill=X)
        Button(root, text="Константа равновесия", font=tkFont.Font(size=fs), command=lambda: self.kravl()).pack(fill=X)
        Button(root, text="График LnK(T)", font=tkFont.Font(size=fs), command=lambda: self.graph()).pack(fill=X)
        Button(root, text="Меню", font=tkFont.Font(size=fs), command=lambda: self.menu() ).pack(fill=X)

    def menu(self):
        self.root.destroy()
        self.Init.menu()

    def doli(self):
        o = OP(self.root, self.num, "doli", self.T, self.Init)
    def graph(self):
        o = OP(self.root, self.num, "plotl", self.T, self.Init)

    def Engac(self):
        o = OP(self.root, self.num, "engac", self.T, self.Init)

    def ravnl(self):
        o = OP(self.root, self.num, "ravl", self.T, self.Init)

    def kravl(self):
        o = OP(self.root, self.num, "kravl", self.T, self.Init)
    def is_state(self):
        compounds=[]
        with open(self.pathR,"r") as f:
            for x in json.load(f)["R"]:
                compounds.append(x[1])
        with open(self.pathR, "r") as f:
            for x in json.load(f)["P"]:
                compounds.append(x[1])
        flag = False
        for x in compounds:
            if x=="Solid":
                flag=True
            else:
                flag=False
                break
        if flag:
            return None

        flag = False
        for x in compounds:
            if x=="Liquid" or x=="Solid":
                flag=True
            else:
                flag=False
                break
        if flag:
            return "L"

        for x in compounds:
            if x=="Gas" or x=="Solid":
                flag=True
            else:
                flag=False
                break
        if flag:
            return "G"
        else:
            return None

    def run(self):
        self.root.mainloop()