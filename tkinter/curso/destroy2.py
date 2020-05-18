from tkinter import *
from tkinter.ttk import *

root = Tk()

btn1 = Button(root, text="Button 1")
btn1.pack(pady = 10)

btn2 = Button(root, text="Button 2")
btn2.pack(pady = 10)

btn1.after(3000, btn1.destroy)
btn2.after(3000, btn2.destroy)

mainloop()