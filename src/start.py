from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import json
from reaction import Err
import time as t


class start:
    height_label=3

    def __init__(self,a):
        self.Init = a
        self.root = Tk()
        self.root.geometry("500x800")
        self.root.minsize(500, 800)
        self.root.maxsize(500, 800)
        self.root.title("Главное меню")
        self.root.iconbitmap("icon.ico")
        self.root.configure(background="gray")
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Ввести новую реакцию", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.react).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="История реакций", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.history).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="FAQ", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.faq).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Выход", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.root.destroy).pack()
        self.run()

    def faq(self):
        t = Toplevel(self.root)
        t.grab_set()
        w, h = 800, 800
        t.geometry(f"{w}x{h}")
        t.maxsize(w, h)
        t.minsize(w, h)
        t.title("Информация для пользователя")
        with open("FAQ.txt","r") as f:
            text = Text(t, value=f.read(), font=("Times New Roman", 16), height=6).pack(side=TOP, fill=X)
            scroll = Scrollbar(t, command=text.yview)
            scroll.pack(side=LEFT, fill=Y)
            text.config(yscrollcommand=scroll.set)
        Button(t, text="OK", font=("Times New Roman", 18), command=t.destroy()).pack(side=BOTTOM, fill=X)

    def react(self):
        self.root.destroy()
        self.Init.reaction()

    def history(self):
        h=Toplevel(self.root)
        h.grab_set()
        h.geometry("400x200")
        h.minsize(200, 200)
        h.maxsize(400, 200)
        h.title("История")
        f=self.finder(h)
        com=ttk.Combobox(h, state="readonly",values=f, width=50)
        if f != None:
            com.current(0)
            com.pack()
            Button(h, text="Просмотреть информацию", command=lambda: self.save_info_and_die(com)).pack()


    def save_info_and_die(self,com):
        F=0
        for key, value in self.djs.items():
            if com.get() == str(value):
                F = self.remove_non_numbers(key)
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

    def get_file_paths(self):
        file_paths = []
        for root, directories, files in os.walk("Reactions"):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def run(self):
        self.root.mainloop()
