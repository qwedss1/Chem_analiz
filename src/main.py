import tkinter as tk
from tkinter import ttk
import interface

class pr:
    def __init__(self):
        self.inter=interface.IF()
        
    @property
    def A(self):
        return self.inter.A
    @property
    def B(self):
        return self.inter.B
    @property
    def C(self):
        return self.inter.C
    @property
    def D(self):
        return self.inter.D
    
    @property
    def A_c(self):
        return self.inter.A_c
    @property
    def B_c(self):
        return self.inter.B_c
    @property
    def C_c(self):
        return self.inter.C_c
    @property
    def D_c(self):
        return self.inter.D_c
prog=pr()
tk.mainloop()
