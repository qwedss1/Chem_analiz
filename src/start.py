from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import json

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
        Button(self.root, text="Ввести новую реакцию", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.react).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="История реакций", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.history).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="FAQ", height=5, width=20, relief="raised", font=tkFont.Font(size=16)).pack()
        Label(self.root, height=self.height_label, background="gray").pack()
        Button(self.root, text="Выход", height=5, width=20, relief="raised", font=tkFont.Font(size=16), command=self.root.destroy).pack()
        self.run()

    def react(self):
        self.root.destroy()
        self.a.reaction()

    def history(self):
        h=Toplevel(self.root)
        h.grab_set()
        h.geometry("200x200")
        h.minsize(200, 200)
        h.maxsize(200, 200)
        h.title("История")
        com=ttk.Combobox(h, state="readonly",values=self.finder())
        com.current(0)
        com.pack()

    def finder(self):
        li = self.get_file_paths()
        for x in li:
            if "Calcu.json" not in x:
                li.remove(x)
        djs = {}
        li1=[]
        for x in li:
            x = self.convert_path(x)
            li1.append(x)
        print(li1)
        for x in li1:
            with open(x, "a") as f:
                print(x)
                djs[x] = json.load(f)["Reaction"]
        self.djs = djs
        return list[djs.values()]

    def get_file_paths(self):
        file_paths = []
        for root, directories, files in os.walk("Reactions"):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)
        return file_paths

    def convert_path(self,path):
        return path.replace('\\', '/')

    def run(self):
        self.root.mainloop()
