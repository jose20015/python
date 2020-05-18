from tkinter import *

tela = Tk()
tela.title("Aula 2")
tela.iconphoto(True, PhotoImage(file='img/whatsappicon2.png'))


#tela.iconbitmap("img/whatsappicon.icon")

#redifinir o tamanho da tela
#tela.geometry("500x250+500+500")
#with: higt 500x250 posição: +200+200
#tela.resizable(False, False) #desativar esticar a tela
#tela.maxsize(width = 500, height = 500)
#tela.minsize(width = 500, height = 500)
#tela.state("iconic") #inicia a tela minizada
#tela.state("zoomed") # inicia a tela maximizada
tela.mainloop()