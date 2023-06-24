from mmoresolve import ms
from tkinter import *


class OP:
    def __init__(self,root, num, code, T, Init):
        if code=="engac":
            self.a=Engac(T, Init, 200, 100, root)


class MM:
    def made(self, top, w, h, t):
        self.root=Toplevel(top)
        root=self.root
        root.geometry(f"{w}x{h}")
        root.title(t)
        root.minsize(w, h)
        root.maxsize(w, h)
        self.run()
        self.done(root)

    def run(self):
        self.root.mainloop()

    def done(self,a):
        pass


class Engac(MM):
    def __init__(self, t, inr, w, h, top):
        self.Init=inr
        self.T=t
        self.made(top, w, h, "Энергия Активации")

    def done(self, r1):
        root=Toplevel(r1)
        w,h=200,400
        root.geometry(f"{w}x{h}")
        root.minsize(w,h)
        root.maxsize(w,h)
        Label(root, text="Введите k и A0 соответсвующе", justify="center").pack()
        e1 = Entry(root)
        e2 = Entry(root)
        e1.pack(side=LEFT)
        e1.pack(side=LEFT)
        Button(text="OK", command=lambda: self.Next(root, e1.get(), e2.get(), r1)).pack()

    def Next(self, root, k, A0, parentt):
        root.destroy()
        Label(parentt, text=f"{ms.engac(A0,k,self.T)} Дж", justify="center", font =("Times New Roman", 16)).pack(fill=X)







