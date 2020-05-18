from tkinter import*

programar= Tk()
programar.title("Caixa de Texto")

programar_fontePadrao = ("Arial", "10")

programar_titulo = Label(programar, text="Dados do usuário", font=("Arial", "10", "bold") )
programar_titulo.pack()

programar_nome = Label(programar,text="Nome", font=programar_fontePadrao)
programar_nome.pack(side=LEFT)

programar_nomeLabel = Entry(programar)
programar_nomeLabel["width"] = 30
programar_nomeLabel["font"] = programar_fontePadrao
programar_nomeLabel.pack(side=LEFT)

programar_nota1 = Label(programar,text="Nota 1", font=programar_fontePadrao)
programar_nota1.pack(side=BOTTOM)
programar_nota1Label = Entry(programar_nota1)
programar_nota1Label["width"] = 30
programar_nota1Label["font"] = programar_fontePadrao
programar_nota1Label.pack(side=BOTTOM)

programar_nota2 = Label(programar,text="Nota 2", font=programar_fontePadrao)
programar_nota1.pack(side=LEFT)

programar_nota3 = Label(programar,text="Nota 3", font=programar_fontePadrao)
programar_nota1.pack(side=LEFT)
