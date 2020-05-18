from tkinter import *
from tkinter.ttk import *

master = Tk()

#grid method to arrange labels in respecive
#rows and columns as specified
l1 = Label(master, text = "Height")
l2 = Label(master, text = "Width")

#entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column =1, pady = 2)

#ckeckbutton widget
c1 = Checkbutton(master, text = "Prevserve")
c1.grid(row = 2, column = 0, stick = W, columnspan = 2)

#adding image image (remember image should be PNG and not JPG)
img = PhotoImage(file = r"whatsappicon.png")
img1 = img.subsample(2,2)

# setting image with help of label
Label(master, image = img1).grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5)

#button widget
b1 = Button(master, text = "Zoom in")
b2 = Button(master, text = "Zoom out")

#arrangin button widgets
b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)

master.mainloop()



