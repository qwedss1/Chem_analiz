'''
В этом файле нужно описать всю рограмму:
ВСЕ ИМПОРТЫ МОДУЛЕЙ
модули:(надо выделить!!!)
НУжно рассинхронить поля для ввода молей!
Нужно сделать стех смесь кнопкой
Нужено застсвить работать флаг(кнопку?) стех смесь
нужно заставить программу выводить правильный словарь
Нужно написать модуль возвращающий словарь отформатированный верно пример - А+В=с-> {"A":[c_A,state],"B":[],C:[]}(D нет в словаре)
    НУЖНО составить скрепер ,который соберет информацию с сайта(его еще нужно выбрать)
        Пусть он будет динамически вытаскивать информацию с сайта при запросе, затем он будет помещать эту информацию в БД ,которая изначально пуста. 
Нужно создать модуль для нахождения z-ok
нужно создать термодинамический модуль
нужно создать модуль графиков
нужно приготовить тесты
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

        self.A=None
        self.B=None
        self.C=None
        self.D=None
        
        self.A_c=None
        self.B_c=None
        self.C_c=None
        self.D_c=None
        
        self.As=None
        self.Bs=None
        self.Cs=None
        self.Ds=None

        tk.Entry(textvariable=self.A).grid(row=2,column=0,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=1)
        
        tk.Entry(textvariable=self.B).grid(row=2,column=2,padx=30,pady=10)
        
        tk.Label(text="=").grid(row=2,column=3)
        
        tk.Entry(textvariable=self.C).grid(row=2,column=4,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=5)
        
        tk.Entry(textvariable=self.D).grid(row=2,column=6,padx=30,pady=10)
        
        val=["Gas","Solid","Liquid"]
        self.A_s=ttk.Combobox(values=val,state="readonly",textvariable=self.As)
        self.A_s.current(0)
        self.A_s.grid(row=3,column=0)
        
        self.B_s=ttk.Combobox(values=val,state="readonly",textvariable=self.Bs)
        self.B_s.current(0)
        self.B_s.grid(row=3,column=2)
        
        self.C_s=ttk.Combobox(values=val,state="readonly",textvariable=self.Cs)
        self.C_s.current(0)
        self.C_s.grid(row=3,column=4)
        
        self.D_s=ttk.Combobox(values=val,state="readonly",textvariable=self.Ds)
        self.D_s.current(0)
        self.D_s.grid(row=3,column=6)
        
        tk.Label(text="moles:").grid(row=4,column=0,columnspan=7)
        
        tk.Entry(textvariable=self.A_c).grid(row=5,column=0)
        
        tk.Entry(textvariable=self.B_c).grid(row=5,column=2)
        
        tk.Entry(textvariable=self.C_c).grid(row=5,column=4)
        
        tk.Entry(textvariable=self.D_c).grid(row=5,column=6)
        
        self.Flag=ttk.Checkbutton(text="Стехиометрическая смесь",command=self.changed_Flag)
        self.Flag.grid(row=6, column=3)
        tk.Button(text="Ready",command=self.com_red).grid(row=10,column=0,stick="we",columnspan=7)
    def com_red(self):
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
        d[self.inter1.A.get()]=[self.inter1.A_c,self.inter1.As]
        d[self.inter1.B]=[self.inter1.B_c,self.inter1.Bs]
        d[self.inter1.C]=[self.inter1.C_c,self.inter1.Cs]
        d[self.inter1.D]=[self.inter1.D_c,self.inter1.Ds]
        
        print(d)
        
p=prog()      
tk.mainloop()