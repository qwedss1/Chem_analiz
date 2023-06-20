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
        root = self.root
        Label(self.root, text="Введите k и A0").pack()
