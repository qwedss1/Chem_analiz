from mmoresolve import ms
from tkinter import *


class OP:
    def __init__(self,root, num, code, T, Init):
        if code=="engac":
            self.a = Engac(T, Init, 500, 300, root)
        elif code=="ravl":
            self.a = Ravnl(num, 500, 300, root)
        elif code == "kravl":
            self.a = Krovl(num, 500, 100, root)
        elif code=="plotl":
            self.a=Plotnik(num, 500, 100, root)


class Engac():
    def __init__(self, T, init, w, h, root):
        self.root=Toplevel(root)
        rt=self.root
        rt.title("Энергия Активации")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
        rt.grab_set()
        Label(rt,text="Используйте форму записи 2.2*10^-20 = 2.2e-20", font=("Times new roman", 16)).pack()
        Label(rt,text=f"k при T={T}", font=("Times new roman", 16)).pack()
        k=Entry(rt,font=("Times new roman", 16))
        k.pack()
        Label(rt, text="A0",font=("Times new roman", 16)).pack()
        A0 = Entry(rt,font=("Times new roman", 16))
        A0.pack()
        l=Label(rt,font=("Times new roman", 16))
        Button(rt,font=("Times new roman", 16),text="Рассчёт", command=lambda: self.sol(l, T, k.get(), A0.get())).pack()
        Label(rt, font=("Times new roman", 30)).pack()
        l.pack()

    def sol(self, l, T, k, A0):
        l.config(text=f"Ea= {ms.engac(float(A0), float(k), float(T))}")


class Ravnl:
    def __init__(self, num, w, h, root):
        self.root = Toplevel(root)
        sen=ms.EqMolLStech(num)
        rt=self.root
        rt.title("Равновесные моли стех смеси")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
        rt.grab_set()
        fs=20
        Label(rt, text=f"z={round(sen[0],3)}", font=("Times new roman", fs)).pack()
        print(sen)
        for x in sen[1]:
            Label(rt, text=f"[{x[0]}]={round(x[1],3)}", font=("Times new roman", fs)).pack()
        Button(rt, text="OK", command=lambda: rt.destroy(), font=("Times new roman", fs)).pack(side=BOTTOM)

class Krovl:
    def __init__(self, num, w, h, root):
        self.root = Toplevel(root)
        rt=self.root
        rt.title("Равновесия константа")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
        rt.grab_set()
        Label(rt, text=f"K={ms.Kravn(num)}", font=("Times new roman", 25)).pack()
        Button(rt, text="OK", command=lambda: rt.destroy(), font=("Times new roman", 25)).pack(side=BOTTOM)

class Plotnik:
    def __init__(self, num, w, h, root):
        self.root = Toplevel(root)
        rt=self.root
        rt.title("Данные")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
        rt.grab_set()
        Label(rt, text=f"A0", font=("Times new roman", 25)).pack()
        e=Entry(rt, font=("Times new roman", 25))
        e.pack()
        Button(rt, text="Построение", command=lambda: self.Plot(rt, e.get(),num), font=("Times new roman", 25)).pack()
        Button(rt, text="Выход", command=lambda: rt.destroy(), font=("Times new roman", 25)).pack(side=BOTTOM)

    def Plot(self, rt, A0, num):
        ms.graphik(A0, num)
        rt.destroy()