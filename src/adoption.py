import tkinter as tk
from tkinter import ttk
import json
class windowAd:
    def __init__(self):
        self.main=tk.Tk()
        with open('cashew.json') as f:
            self.d=json.load(f)
        
