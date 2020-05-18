from tkinter import *
tela = Tk()

var = StringVar(root)
var.set("one") #initial value

option = OptionMenu(root, var, "one", "tow", "four")
option.pack()

def ok():
    print "value is", var.get()
    master.quit()

button = Button(root, text="OK", command=ok)
button.pack()

root.mainloop()