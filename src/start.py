from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import json
from reaction import Err


class start:
    height_label = 3

    def __init__(self, a):
        self.Init = a
        self.root = Tk()
        self.root.geometry("500x800")
        self.root.minsize(500, 800)
        self.root.maxsize(500, 800)
        self.root.title("Главное меню")
        self.root.iconbitmap("icon.ico")
        self.root.configure(background="gray")
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Ввести новую реакцию", height=5, width=20, relief="raised", font=('Times New Roman', 16), command=self.react).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="История реакций", height=5, width=20, relief="raised", font=('Times New Roman', 16), command=self.history).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="FAQ", height=5, width=20, relief="raised", font=('Times New Roman', 16)).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Выход", height=5, width=20, relief="raised", font=('Times New Roman', 16), command=self.root.destroy).pack()
        self.run()

    def react(self):
        self.root.destroy()
        self.Init.reaction()

    def history(self):
        h = Toplevel(self.root)
        h.grab_set()
        w, f = 450, 100
        h.geometry(f"{w}x{f}")
        h.minsize(w, f)
        h.maxsize(w, f)
        h.title("История")
        f = self.finder(h)
        com = ttk.Combobox(h, state="readonly",values=f, width=50, font=('Times New Roman', 20))
        h.option_add("*TCombobox*Listbox*Font", tkFont.Font(family='Times New Roman', size=28))
        if f:
            com.current(0)
            com.pack()
            Button(h, text="Просмотреть информацию", command=lambda: self.save_info_and_die(com), font=tkFont.Font(size=16)).pack()


    def save_info_and_die(self,com):
        F=0
        for key, value in self.djs.items():
            if com.get()==str(value):
                F=self.remove_non_numbers(key)
                break
        self.root.destroy()
        self.Init.data(F)
        self.del_me()

    def del_me(self):
        del self

    def remove_non_numbers(self,input):
        return ''.join(filter(str.isdigit, input))

    def finder(self,h):
        dj = {}
        l = self.get_file_paths()
        try:
            if l == []:
                raise Err("Нет реакций",self.root)
            else:
                for x in l:
                    if "Calcu.json" in x:
                        with open(x, "r") as f:
                            dj[x] = json.load(f)["Reaction"]
                self.djs = dj
                return list(dj.values())
        except :
            pass

    @staticmethod
    def get_file_paths():
        file_paths = []
        for root, directories, files in os.walk("Reactions"):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def run(self):
        self.root.mainloop()
