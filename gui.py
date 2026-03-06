from tkinter import *
from tkinter import ttk

def getlinks():
    root.destroy()
    import getlinks


    
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="What to Steal").grid(column=1, row=0)
ttk.Button(frm, text="Links", command=getlinks).grid(column=0, row=2)
ttk.Button(frm, text="Names", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Dialogue", command=root.destroy).grid(column=2, row=2)
root.mainloop()


