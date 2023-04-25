import tkinter as tk
def com():
    txt=entry.get()
    lb1=tk.Label(
        bg="#FFAABB",
        fg="#FFFFFF",
        text=txt
    )
    lb1.pack()
window=tk.Tk()
label = tk.Label(
    text="There was not good words, but nooooow....",
    foreground="white",  
    background="blue",
    width=155,
    height=20,
)
label.pack()
button1=tk.Button(
    text="clk meee!",
    bg="#FFFFFF",
    fg="#000000",
    command=com
)
entry=tk.Entry(
    bg="#FFFFFF",
    fg="#ABCDF0"
)
button1.pack()
entry.pack()
frame=tk.Frame()
frame.pack()
frame2=tk.Frame()
frame2.pack(side=tk.LEFT)


label2=tk.Label(master=frame2,text="you opinion?",bg="white",fg="black")
label2.pack()
button12=tk.Button(master=frame,text="0000")
button12.pack()
window.mainloop()