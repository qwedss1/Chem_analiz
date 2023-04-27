import tkinter as tk
from tkinter import ttk

class interface:
    def __init__(self):  
        self.win=tk.Tk() 
        self.win.title("Chem-analizis")
        
        tk.Label(text="Химическая реакция:").grid(row=0,column=0,stick="we",columnspan=7)
        
        tk.Label(text="Вещество А").grid(row=1,column=0)
        tk.Label(text="Вещество B").grid(row=1,column=2)
        tk.Label(text="Вещество C").grid(row=1,column=4)
        tk.Label(text="Вещество D").grid(row=1,column=6)
        tk.Entry().grid(row=2,column=0,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=1)
        
        tk.Entry().grid(row=2,column=2,padx=30,pady=10)
        
        tk.Label(text="=").grid(row=2,column=3)
        
        tk.Entry().grid(row=2,column=4,padx=30,pady=10)
        
        tk.Label(text="+").grid(row=2,column=5)
        
        tk.Entry().grid(row=2,column=6,padx=30,pady=10)
        
        val=["Gas","Solid","Liquid"]
        self.A=ttk.Combobox(values=val,state="readonly")
        self.A.current(0)
        self.A.grid(row=3,column=0)
        
        self.B=ttk.Combobox(values=val,state="readonly")
        self.B.current(0)
        self.B.grid(row=3,column=2)
        
        self.C=ttk.Combobox(values=val,state="readonly")
        self.C.current(0)
        self.C.grid(row=3,column=4)
        
        self.D=ttk.Combobox(values=val,state="readonly")
        self.D.current(0)
        self.D.grid(row=3,column=6)
        
        tk.Label(text="moles:").grid(row=4,column=0,columnspan=7)
        
        self.A_c=tk.Entry()
        self.A_c.grid(row=5,column=0)
        
        self.B_c=tk.Entry()
        self.B_c.grid(row=5,column=2)
        
        self.C_c=tk.Entry()
        self.C_c.grid(row=5,column=4)
        
        self.C_c=tk.Entry()
        self.C_c.grid(row=5,column=6)
        
        self.Flag=ttk.Checkbutton(text="Стехиометрическая смесь")
        self.Flag.grid(row=6, column=3)
        tk.Button(text="Ready").grid(row=10,column=0,stick="we",columnspan=7)

i=interface()
tk.mainloop()