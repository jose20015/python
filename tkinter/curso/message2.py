from tkinter import *

root = Tk()
variable = StringVar(root)
variable.set("one") #default value

w = OptionMenu(root, variable, "one", "tow", "three")
w.pack()

root.mainloop()