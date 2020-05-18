from tkinter import *
root = Tk()

MODES = [
         ("Monochrome", "1"),
         ("Grayscale", "L"),
         ("True color", "RGB"),
         ("Color separation", "CMYK"),
        ]

v = StringVar()
v.set("L") #initialize

for text, mode in MODES:
    b = Radiobutton(root, text=text, variable = v, value=mode, justify=RIGHT, padx=60,pady=100)
    b.pack(anchor=W)
mainloop()