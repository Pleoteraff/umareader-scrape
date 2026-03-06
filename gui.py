from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="AAAAA").grid(column=1, row=0)
ttk.Button(frm, text="Links", command=root.destroy).grid(column=0, row=2)
ttk.Button(frm, text="Names", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Dialogue", command=root.destroy).grid(column=2, row=2)
root.mainloop()