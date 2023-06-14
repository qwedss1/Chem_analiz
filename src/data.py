from tkinter import *
import tkinter.font as tkFont
from solve import *


class Data:

    def __init__(self,d,num):
        self.Init = d
        self.s = solve(num)
        self.mainwin()
        self.run()

    def mainwin(self):
        self.root=Tk()
        fontsize=20
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
        Label(root, text=f"T={int(self.s.temp)} K", justify="center", font=tkFont.Font(size=fontsize), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fontsize)).pack()
        Label(root, text=f"dHT={round(self.s.dH*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fontsize), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fontsize)).pack()
        Label(root, text=f"dGT={round(self.s.dG*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fontsize), width=25).pack()
        Label(root, width=25, font=tkFont.Font(size=fontsize)).pack()
        Label(root, text=f"dST={round(self.s.dS*4.184,3)} Дж", justify="center", font=tkFont.Font(size=fontsize), width=25).pack()
        Label(root, height=1, background="gray").pack()
        Button(text="Изменить температуру", command=self.change_T, font=tkFont.Font(size=fontsize-2), width=25, height=1, justify="center").pack()
        Button(text="Дополнительный рассчет", command=self.additional, font=tkFont.Font(size=fontsize-2), width=25, height=1, justify="center").pack()
        Button(text="Меню", command=self.Menu, font=tkFont.Font(size=fontsize-2), width=25, height=1, justify="center").pack()
        Button(text="Выход", command=lambda: root.destroy(), font=tkFont.Font(size=fontsize-2), width=25, height=1, justify="center").pack()

    def change_T(self):
        pass

    def additional(self):
        pass

    def Menu(self):
        pass

    def run(self):
        self.root.mainloop()