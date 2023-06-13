from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class start:
    height_label=3

    def __init__(self,a):
        self.a=a
        self.root=Tk()
        self.root.geometry("500x800")
        self.root.minsize(500, 800)
        self.root.maxsize(500, 800)
        self.root.title("Главное меню")
        self.root.iconbitmap("icon.ico")
        self.root.configure(background="gray")
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Ввести новую реакцию", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.b1func).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="История реакций", height=5, width=20, relief="raised", font=tkFont.Font(size=16)).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="FAQ", height=5, width=20, relief="raised", font=tkFont.Font(size=16)).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Выход", height=5, width=20, relief="raised", font=tkFont.Font(size=16)).pack()
        self.run()

    def b1func(self):
        self.root.destroy()
        self.a.stage2()

    def run(self):
        self.root.mainloop()
