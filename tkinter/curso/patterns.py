from tkinter import *

master = Tk()

listbox = Listbox(master)
listbox.pack()

listbox.insert(END, "a list entry")

for item in ["one", "tow", "there", "four"]:
    listbox.insert(END, item)

#listbox.delete(0, END)



master.mainloop()