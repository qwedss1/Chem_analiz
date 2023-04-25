import tkinter as tk

class interface:
    def __init__(self):
        self.window=tk.Tk()
        self.lab_lab=tk.Label(text="Химическая реакция:",width=200,height=5)
        self.lab_lab.pack()
        
        self.fabcd=tk.Frame()
        self.fabcd.pack(side=tk.LEFT)
        
        self.eA=tk.Entry(width=10)
        self.eA.pack(side=tk.LEFT)
        self.lbP=tk.Label(text="+",width=1)
        self.lbP.pack(side=tk.LEFT())
i=interface()
tk.mainloop()