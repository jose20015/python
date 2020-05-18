from tkinter import *

tela = Tk()
largura = 500
altura = 500

#sabendo altura e largura default da tela
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()
#print("largura: ", largura_screen)
#print("altura: ", altura_screen)

posicao_x = largura_screen / 2 - largura / 2
posicao_y = altura_screen / 2 - altura / 2
tela.geometry("%dx%d+%d+%d"%(largura, altura, posicao_x, posicao_y))


tela.mainloop()