from tkinter import *

def sel():
    selection = "You selected the " + str(var.get())
    op=str(var.get())
    label.config(text = op )

root = Tk()
var = StringVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value="oi",
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(root, text="Option 2", variable=var, value="lo",
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(root, text="Option 3", variable=var, value="hu",
                  command=sel)
R3.pack( anchor = W)

label = Label(root)
label.pack()
root.mainloop()
