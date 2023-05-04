'''
В этом файле нужно описать всю рограмму:
ВСЕ ИМПОРТЫ МОДУЛЕЙ
модули:(надо выделить!!!)
'''

import tkinter as tk
from tkinter import ttk

class IF:
    def __init__(self):  
        self.win=tk.Tk() 
        self.win.title("Chem-analizis")
        tk.Label(text="Химическая реакция:").grid(row=0,column=0,stick="we",columnspan=7)
        
        tk.Label(text="Вещество А").grid(row=1,column=0)
        tk.Label(text="Вещество B").grid(row=1,column=2)
        tk.Label(text="Вещество C").grid(row=1,column=4)
        tk.Label(text="Вещество D").grid(row=1,column=6)
        
        self.A=''
        self.B=''
        self.C=''
        self.D=''
        
        self.A_c=0
        self.B_c=0
        self.C_c=0
        self.D_c=0
        
        tk.Entry(textvariable=self.A).grid(row=2,column=0,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=1)
        
        tk.Entry(textvariable=self.B).grid(row=2,column=2,padx=30,pady=10)
        
        tk.Label(text="=").grid(row=2,column=3)
        
        tk.Entry(textvariable=self.C).grid(row=2,column=4,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=5)
        
        tk.Entry(textvariable=self.D).grid(row=2,column=6,padx=30,pady=10)
        
        val=["Gas","Solid","Liquid"]
        self.A_s=ttk.Combobox(values=val,state="readonly")
        self.A_s.current(0)
        self.A_s.grid(row=3,column=0)
        
        self.B_s=ttk.Combobox(values=val,state="readonly")
        self.B_s.current(0)
        self.B_s.grid(row=3,column=2)
        
        self.C_s=ttk.Combobox(values=val,state="readonly")
        self.C_s.current(0)
        self.C_s.grid(row=3,column=4)
        
        self.D_s=ttk.Combobox(values=val,state="readonly")
        self.D_s.current(0)
        self.D_s.grid(row=3,column=6)
        
        tk.Label(text="moles:").grid(row=4,column=0,columnspan=7)
        
        self.A_c=tk.Entry(textvariable=self.A_c).grid(row=5,column=0)
        
        self.B_c=tk.Entry(textvariable=self.B_c).grid(row=5,column=2)
        
        self.C_c=tk.Entry(textvariable=self.C_c).grid(row=5,column=4)
        
        self.D_c=tk.Entry(textvariable=self.D_c).grid(row=5,column=6)
        
        self.Flag=ttk.Checkbutton(text="Стехиометрическая смесь",command=self.changed_Flag)
        self.Flag.grid(row=6, column=3)
        tk.Button(text="Ready",command=self.com_red).grid(row=10,column=0,stick="we",columnspan=7)
    def com_red(self):
        self.A_s=self.A_s.get()
        self.B_s=self.B_s.get()
        self.C_s=self.C_s.get()
        self.D_s=self.D_s.get()
        
        self.win.destroy()
        p.next1()
    def changed_Flag(self):
        pass
'''
функция обрабатывающая флаг стех смесь
'''
        

class prog:
    def __init__(self):
        self.inter1=IF()
    def next1(self):
        d=dict()
        d[self.inter1.A]=[self.inter1.A_c,self.inter1.A_s]
        d[self.inter1.B]=[self.inter1.B_c,self.inter1.B_s]
        d[self.inter1.C]=[self.inter1.C_c,self.inter1.C_s]
        d[self.inter1.D]=[self.inter1.D_c,self.inter1.D_s]
        
        print(d)
        
p=prog()      
tk.mainloop()