from tkinter import *
   
class app:
    def __init__(self, master=None):

        self.widget1 = Frame(master)
        self.widget1.pack()

        self.container1= Frame(master)
        self.container1["pady"] = 10
        self.container1["padx"]= 20
        self.container1.pack()

        self.container2= Frame(master)
        self.container2["pady"] = 10
        self.container2["padx"]= 20
        self.container2.pack()

        self.msgLabel = Label(self.widget1, text="Teste ")
        self.msgLabel["font"] = ("Calibri", "9", "italic")
        self.msgLabel.pack ()

        self.msgLabel = Label(self.container1, text="Nome: ")
        self.msgLabel["font"] = ("Calibri", "9", "italic")
        self.msgLabel.pack (side=LEFT)

        self.msg = Entry(self.container1)
        self.msg["font"] = ("Calibri", "9", "italic")
        self.msg.pack (side=LEFT)
        
        self.sair = Button(self.container1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "9")
        self.sair["width"] = 10
        self.sair["command"] = self.ola
        self.sair.pack (side=LEFT)

        self.texto= Label(self.container2, text="")
        self.texto.pack(side= BOTTOM)

    def ola(self):
        self.texto["text"] = "Olá %s" %self.msg.get()   
   
botao = Tk()
botao.title("Bem Vindo")
app(botao)
botao.mainloop()

