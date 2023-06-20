from mmoresolve import ms
from tkinter import *


class OP:
    def __init__(self, num, code, a):
        if code=="engac":
            self.a=engac(a,200,100,"Энергия активации")


class MM:
    def __init__(self, inr,w ,h, t):
        self.Init=inr
        self.made(w, h, t)

    def made(self, w, h, t):
        self.root=Tk()
        root=self.root
        root.geometry(f"{w}x{h}")
        root.title(t)
        root.minsize(w, h)
        root.maxsizesize(w, h)
        self.run()
        self.done()

    def run(self):
        self.root.mainloop()

    def done(self):
        pass


class engac(MM):
    def done(self):
        self.ASK()
    def ASK(self):
        root=Toplevel(self.root)
        root.geometry(f"{200}x{200}")
        root.minsize(200, 200)
        root.maxsizesize(200, 200)
        Label(root, text="Введите k и A0 соответсвующе", justify="center").pack()
        e1 = Entry(root)
        e2 = Entry(root)
        e1.pack(side=LEFT)
        e1.pack(side=LEFT)
        Button(text="OK", command=lambda: self.Next(root,e1.get(),e2.get())).pack()

    def Next(self, a, A, B):
        a.destroy()






