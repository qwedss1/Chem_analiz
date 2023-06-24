from mmoresolve import ms
from tkinter import *


class OP:
    def __init__(self,root, num, code, T, Init):
        if code=="engac":
            self.a=Engac(T, Init, 500, 300, root)
        elif code=="ravl":
            self.a=AskSenya(num, 500, 300, root)


class Engac():
    def __init__(self, T, init, w, h, root):
        self.root=Toplevel(root)
        rt=self.root
        rt.title("Энергия Активации")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
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


class AskSenya:
    def __init__(self, num, w, h, root):
        self.root = Toplevel(root)
        sen=ms.EqMolLStech(num)
        rt=self.root
        rt.title("Энергия Активации")
        rt.geometry(f"{w}x{h}")
        rt.minsize(w, h)
        rt.maxsize(w, h)
        Label(rt, text=f"z={sen[0]}").pack()
        print(sen)
        for x in sen[1]:
            Label(rt, text=f"[{x[0]}]={x[1]}").pack()
        Button(rt, text="OK", command=lambda: rt.destroy()).pack()

