from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import os
import json

class start:
    height_label=3

    def __init__(self,a):
        self.Init=a
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
        self.Init.reaction()

    def history(self):
        h=Toplevel(self.root)
        h.grab_set()
        h.geometry("400x200")
        h.minsize(200, 200)
        h.maxsize(400, 200)
        h.title("История")
        com=ttk.Combobox(h, state="readonly",values=self.finder(), width=50)
        com.current(0)
        com.pack()
        Button(h, text="Просмотреть информацию", command=lambda: self.save_info_and_die(com)).pack()

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
        for x in li1:
            with open(x, "r") as f:
                djs[x] = str(json.load(f)["Reaction"])
        self.djs = djs
        ans=[]
        for key, value in djs.items():
            ans.append(value)
        return ans

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
