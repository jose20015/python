from tkinter import *

root = Tk()

w = Scale(root, from_ =0, to =100)
w.pack()

w = Scale(root, from_ =0, to=200, orient=HORIZONTAL)
w.pack()

mainloop()