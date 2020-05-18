from tkinter import *

m = PanedWindow(orient=VERTICAL)
m.pack(fill=BOTH, expand=1)

top = Label(m, text="top pane")
m.add(top)

bottom = Label(m, text="botton pane")
m.add(bottom)

mainloop()