import tkinter as tk

class interface:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("800x200")        
        self.lab_lab=tk.Label(text="Химическая реакция:",width=100,height=5)
        self.lab_lab.pack()
        
        self.A=tk.Entry()
        self.A.pack(side=tk.LEFT, padx=10,pady=10)
        
        self.LP=tk.Label(text="+")
        self.LP.pack(side=tk.LEFT,padx=1,pady=1)
        
        self.B=tk.Entry()
        self.B.pack(side=tk.LEFT, padx=10,pady=10)
        
        self.LE=tk.Label(text="=")
        self.LE.pack(side=tk.LEFT,padx=1,pady=1)
        
        self.C=tk.Entry()
        self.C.pack(side=tk.LEFT, padx=10,pady=10)
        
        self.LP=tk.Label(text="+")
        self.LP.pack(side=tk.LEFT,padx=1,pady=1)
        
        self.D=tk.Entry()
        self.D.pack(side=tk.LEFT, padx=10,pady=10)
        
        self.f=tk.Frame()
        self.f.pack()
        
        
i=interface()
tk.mainloop()