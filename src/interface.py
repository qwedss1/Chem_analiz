import tkinter as tk
from tkinter import ttk

class interface:
    def __init__(self):
        self.win=tk.Tk()
        self.win.geometry("1000x200")    
        
        tk.Label(text="Химическая реакция:",height=10,width=100).pack()
        
        tk.Entry().pack(side=tk.LEFT)
        
        tk.Label(text="+").pack(side=tk.LEFT)
        
        tk.Entry().pack(side=tk.LEFT)
        
        tk.Label(text="=").pack(side=tk.LEFT)
        
        tk.Entry().pack(side=tk.LEFT)
        
        tk.Label(text="+").pack(side=tk.LEFT)
        
        tk.Entry().pack(side=tk.LEFT)

        tk.Button(text="Ready").pack(side=tk.BOTTOM,fill=tk.BOTH)
        
        
        
i=interface()
tk.mainloop()