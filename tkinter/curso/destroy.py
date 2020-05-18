from tkinter import *
from tkinter.ttk import *

root = Tk()

btn1 = Button(root, text = "Button 1", command=root.destroy)
btn1.pack(pady=10)

btn2 = Button(root, text = "Button 2", command=btn1.destroy)
btn2.pack(pady = 10)

mainloop()