import tkinter as tk
from tkinter import ttk

class windowIn:
    def __init__(self):  
        self.main=tk.Tk() 
        self.main.title("Chem-analizis")
        tk.Label(self.main,text="Химическая реакция:").grid(row=0,column=0,stick="we",columnspan=7)
        
        tk.Label(self.main,text="Вещество А").grid(row=1,column=0)
        tk.Label(self.main,text="Вещество B").grid(row=1,column=2)
        tk.Label(self.main,text="Вещество C").grid(row=1,column=4)
        tk.Label(self.main,text="Вещество D").grid(row=1,column=6)

        self.A=tk.Entry(self.main)
        self.A.grid(row=2,column=0,padx=30,pady=10)
        
        tk.Label(self.main,text="+").grid(row=2,column=1)
        
        self.B=tk.Entry(self.main)
        self.B.grid(row=2,column=2,padx=30,pady=10)
        
        tk.Label(self.main,text="=").grid(row=2,column=3)
        
        self.C=tk.Entry(self.main)
        self.C.grid(row=2,column=4,padx=30,pady=10)
        
        tk.Label(self.main,text="+").grid(row=2,column=5)
        
        self.D=tk.Entry(self.main)
        self.D.grid(row=2,column=6,padx=30,pady=10)
        
        val=["Gas","Solid","Liquid"]
        self.A_s=ttk.Combobox(self.main,values=val,state="readonly")
        self.A_s.current(0)
        self.A_s.grid(row=3,column=0)
        
        self.B_s=ttk.Combobox(self.main,values=val,state="readonly")
        self.B_s.current(0)
        self.B_s.grid(row=3,column=2)
        
        self.C_s=ttk.Combobox(self.main,values=val,state="readonly")
        self.C_s.current(0)
        self.C_s.grid(row=3,column=4)
        
        self.D_s=ttk.Combobox(self.main,values=val,state="readonly")
        self.D_s.current(0)
        self.D_s.grid(row=3,column=6)
        
        tk.Label(self.main,text="moles:").grid(row=4,column=0,columnspan=7)
        
        self.A_c=tk.Entry(self.main)
        self.A_c.grid(row=5,column=0)
        
        self.B_c=tk.Entry(self.main)
        self.B_c.grid(row=5,column=2)
        
        self.C_c=tk.Entry(self.main)
        self.C_c.grid(row=5,column=4)
        
        self.D_c=tk.Entry(self.main)
        self.D_c.grid(row=5,column=6)
        
        self.Flag=ttk.Checkbutton(self.main,text="Стехиометрическая смесь",command=self.changed_Flag)
        self.Flag.grid(row=6, column=3)
        tk.Button(self.main,text="Ready",command=self.com_red).grid(row=10,column=0,stick="we",columnspan=7)
    def com_red(self):
        self.A=self.A.get()
        self.B=self.B.get()
        self.C=self.C.get()
        self.D=self.D.get()
        self.d=dict()
        self.d[self.A]=[self.A_c.get(),self.A_s.get()]
        self.d[self.B]=[self.B_c.get(),self.B_s.get()]
        self.d[self.C]=[self.C_c.get(),self.C_s.get()]
        self.d[self.D]=[self.D_c.get(),self.D_s.get()]
        self.main.destroy()
    def changed_Flag(self):
        pass   
    def run(self):
        self.main.mainloop()
        
