from tkinter import *
root = Tk()

def hello():
    print "hello"

#create a popup menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Undo", command=hello)
menu.add_command(label="Redo", command=hello)

#create a canvas
frame = Frame(root, width=512, heigth=512)
frame.pack()

def poup(event):
    menu.post(event.x_root, event.y_root)

# attach popup to canvas
frame.bind("<Button-3>", poup)