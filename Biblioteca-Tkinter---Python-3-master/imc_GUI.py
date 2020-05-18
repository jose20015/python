from tkinter import *

imc = Tk()
imc.title("IMC")

class app:
    def __init__(self, master=None):

        self.container=Frame(master)
        self.container["padx"]=50
        self.container["pady"]=30
        self.container["bg"]="white"
        self.container.pack()

        self.botao1= Button(self.container, text="O QUE É")
        self.botao1["command"]=self.definicao
        self.botao1["width"]=14
        self.botao1["relief"]= "ridge"
        self.botao1.pack()

        self.botao2= Button(self.container, text="Calcule o seu IMC")
        self.botao2["command"]=self.calculo
        self.botao2["relief"]= "ridge"
        self.botao2.pack()

        self.botao3= Button(self.container, text="Tabela")
        self.botao3["width"]= 14
        self.botao3["command"]=self.tabela
        self.botao3["relief"]= "ridge"
        self.botao3.pack()

        self.botao3= Button(self.container, text="Peso")
        self.botao3["width"]= 14
       # self.botao3["command"]=self.tabela
        self.botao3["relief"]= "ridge"
        self.botao3.pack()

    def tabela(self):
        tbl= Tk()
        tbl.geometry("340x289")
        tbl["bg"]="white"
        self.frame1= Frame(tbl)
        self.frame1.pack()
        self.frame2= Frame(tbl)
        self.frame2.pack()
        self.frame3= Frame(tbl)
        self.frame3.pack()
        self.frame4= Frame(tbl)
        self.frame4.pack()
        self.frame5= Frame(tbl)
        self.frame5.pack()
        self.frame6= Frame(tbl)
        self.frame6.pack()
        self.frame7= Frame(tbl)
        self.frame7.pack()
        self.frame8= Frame(tbl)
        self.frame8.pack()

        self.a=Label(self.frame1, text="        IMC < 17     ", font="Arial 14 ",bg="lightyellow")
        self.a["relief"]= "ridge"
        self.a.pack(side=LEFT)
        self.a.coluna=Label(self.frame1, text=" Muito abaixo do peso", font="Arial 14 ", bg="lightyellow")
        self.a.coluna["relief"]= "ridge"
        self.a.coluna.pack(side=RIGHT)

        self.b=Label(self.frame2, text=" 17< IMC <19", font="Arial 14 ",bg="lightyellow")
        self.b["relief"]= "ridge"
        self.b.pack(side=LEFT)
        self.b.coluna=Label(self.frame2, text="   Abaixo do peso       ", font="Arial 14 ", bg="lightyellow")
        self.b.coluna["relief"]= "ridge"
        self.b.coluna.pack(side=RIGHT)

        self.c=Label(self.frame3, text="   19< IMC <25.8", font="Arial 14 ",bg="lightyellow")
        self.c["relief"]= "ridge"
        self.c.pack(side=LEFT)
        self.c.coluna=Label(self.frame3, text="        No peso ideal     ", font="Arial 14 ", bg="lightyellow")
        self.c.coluna["relief"]= "ridge"
        self.c.coluna.pack(side=RIGHT)

        self.d=Label(self.frame4, text="  26 < IMC < 28  \n", font="Arial 14 ",bg="lightyellow")
        self.d["relief"]= "ridge"
        self.d.pack(side=LEFT)
        self.d.coluna=Label(self.frame4, text="Marginalmente acima \ndo peso", font="Arial 14 ", bg="lightyellow")
        self.d.coluna["relief"]= "ridge"
        self.d.coluna.pack(side=RIGHT)

        self.e=Label(self.frame5, text="    28 < IMC < 30", font="Arial 14 ",bg="lightyellow")
        self.e["relief"]= "ridge"
        self.e.pack(side=LEFT)
        self.e.coluna=Label(self.frame5, text="     Acima do peso      ", font="Arial 14 ", bg="lightyellow")
        self.e.coluna["relief"]= "ridge"
        self.e.coluna.pack(side=RIGHT)

        self.f=Label(self.frame6, text="   30 < IMC < 35 ", font="Arial 14 ",bg="lightyellow")
        self.f["relief"]= "ridge"
        self.f.pack(side=LEFT)
        self.f.coluna=Label(self.frame6, text="         Obesidade I       ", font="Arial 14 ", bg="lightyellow")
        self.f.coluna["relief"]= "ridge"
        self.f.coluna.pack(side=RIGHT)

        self.g=Label(self.frame7, text="  35 < IMC < 40  \n ", font="Arial 14 ",bg="lightyellow")
        self.g["relief"]= "ridge"
        self.g.pack(side=LEFT)
        self.g.coluna=Label(self.frame7, text="          Obesidade II     \n      (Severa)", font="Arial 14 ", bg="lightyellow")
        self.g.coluna["relief"]= "ridge"
        self.g.coluna.pack(side=RIGHT)

        self.h=Label(self.frame8, text="    IMC > 40        \n  ", font="Arial 14 ",bg="lightyellow")
        self.h["relief"]= "ridge"
        self.h.pack(side=LEFT)
        self.h.coluna=Label(self.frame8, text="          Obesidade III    \n   (Mórbida)", font="Arial 14 ", bg="lightyellow")
        self.h.coluna["relief"]= "ridge"
        self.h.coluna.pack(side=RIGHT)
        tbl.mainloop()


    def definicao(self):
        definicao=Tk()
        definicao.title("Definição")
        definicao.geometry("545x189")
        self.defin=Label(definicao, text=" \nO Índice de Massa Corporal (IMC) é o padrão pelo qual você pode ver se seus\n níveis de gordura e peso estão dentro do recomendado pela Organização Mundial\n de Saúde.A fórmula é simples: chega-se ao resultado dividindo o peso da pessoa\n em quilos pela altura em centímetros, elevada ao quadrado.Quando estamos \nacima do peso indicado, nos expomos ao risco de desenvolver vários males, como\n diabetes e problemas cardíacos.Mas lembre-se que quem está abaixo também não \nencontra-se em segurança, já que pode desenvolver doenças – neste caso, devido à subnutrição.\nA ideia é observar o quanto você está distante da meta.Utilize seu resultado como informação\n para orientar novos hábitos. Mas, saiba que, apesar de ser preciso, o resultado deve ser referendado\n por um médico responsável.  \n ")
        self.defin["bg"]="white"
        self.defin.configure(relief="ridge", border=5, bg= "white")
        self.defin.pack()

                   
    def calculo(self, master=None):
        
        calculo=Tk()
        calculo.title("IMC")
        calculo.geometry("440x240")
        self.widget1 = Frame(calculo)
        self.widget1.pack()

        self.container1= Frame(calculo)
        self.container1["pady"] = 20
        self.container1["padx"]= 30
        self.container1.pack()

        self.container2= Frame(calculo)
        self.container2["pady"] = 20
        self.container2["padx"]= 30
        self.container2.pack()
   
        self.altura = Label(self.widget1, text="Calcule seu IMC\nUtilize a calculadora de IMC para visualizar sua situação\n e também verificar se está com o peso ideal para a sua altura. ")
        self.altura["font"] = ("Calibri", "10")
        self.altura.pack ()

        self.peso = Label(self.container1, text="Peso(Kg): ")
        self.peso["font"] = ("Calibri", "9", "italic")
        self.peso.pack (side=LEFT)

        self.peso = Entry(self.container1)
        self.peso["font"] = ("Calibri", "9", "italic")
        self.peso["width"]=8
        self.peso.pack (side=LEFT)

        self.altura = Label(self.container1, text="Altura(m): ")
        self.altura["font"] = ("Calibri", "10", "italic")
        self.altura.pack (side=LEFT)

        self.altura = Entry(self.container1)
        self.altura["font"] = ("Calibri", "9", "italic")
        self.altura["width"]=8
        self.altura.pack (side=LEFT)
       
        self.var= IntVar()
        self.rb1= Radiobutton(self.container2, text="Feminino", variable=self.var, value=1, command= self.botaof)
        self.rb1.pack( anchor = W)
        self.rb2= Radiobutton(self.container2, text="Masculino", variable=self.var, value=2, command=self.botaom)
        self.rb2.pack( anchor = W)

        self.calc = Button(self.container1)
        self.calc["text"] = "IMC"
        self.calc["font"] = ("Calibri", "9")
        self.calc["width"] = 5
        self.calc.pack (side=RIGHT)

    def botaof(self):
        self.calc["command"] = self.fem
        self.calc.pack (side=RIGHT)

    def botaom(self):
        self.calc["command"] = self.mas
        self.calc.pack (side=RIGHT)
        
    def fem(self):
        
        peso = float(self.peso.get())
        alt = float(self.altura.get())
        imc = (peso / (alt*alt))
        pesoideal= (((((alt*100)-152.4)/2.54)*1.7)+49)
        popup= Tk()
        popup.title("Resultado")
        popup.geometry("280x280")
        popup.container=Frame(popup)
        popup.container.pack()
        self.result2= Label(popup.container, text="", font="Arial 15 bold")
        self.result2.configure(relief="ridge", border=5, bg= "white")
        self.result2.pack(pady=10)
        self.pesoideal=Label(popup.container, text="", font="Arial 12 bold")
        self.pesoideal.pack(pady=5)
        self.recomends= Label(popup.container, text="")
        self.recomends.pack()

       
        if (imc < 17): #imc<19
            self.result2["text"]= ("   Muito abaixo do peso\n IMC=  %.1f \n   " %imc)
            self.result2["fg"]="red"
            self.pesoideal["text"]=("\n   Seu peso ideal: %.1f   "%pesoideal)                   
            self.recomends["text"]= ("\nNesse ponto, o corpo magro deixa de ser saudável\n e o organismo fica mais vulnerável a infecções. \nSe o baixo peso persistir, mesmo com alimentação\n normal, procure ajuda médica; a dificuldade\n para engordar pode ser sintoma de alguma doença\n insidiosa, como o diabetes.")
        elif (17 <= imc < 18.49):#19<imc<20.7
            self.result2["text"]= ("   Abaixo do Peso\n  IMC= %.1f   " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\n  Seu peso ideal: %.1f   "%pesoideal) 
            self.recomends["text"]= ("\nNesse ponto, o corpo magro deixa de ser saudável\n e o organismo fica mais vulnerável a infecções. \nSe o baixo peso persistir, mesmo com alimentação\n normal, procure ajuda médica; a dificuldade\n para engordar pode ser sintoma de alguma doença\n insidiosa, como o diabetes.")

        elif (18.49 <= imc < 25.8):#20.7<imc<26.4
            self.result2["text"]= ("   Peso Normal    \n  IMC= %.1f   " %imc)
            self.pesoideal["text"]=("\n   Seu peso ideal: %.1f   "%pesoideal)
            self.recomends["text"]= ("Seu peso está adequado à altura. É importante\n manter a educação alimentar e a atividade física.\n Fique atento caso seu valor esteja perto dos \nlimites para os estágios de Baixo Peso ou \nSobrepeso.")
        elif (25.8 <= imc <27.3):#26.4<imc<27.8
            self.result2["text"]= ("   Marginalmente acima do peso\n IMC= %.1f  " %imc)
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("Esta faixa indica que você está com predisposição\n à obesidade; dependendo do seu histórico familiar\n e pessoal, pode haver um quadro de pré-diabetes\n e hipertensão. Procure orientação médica para\n evitar o próximo estágio, Obesidade 1.\n Quanto mais quilos extras, maior a dificuldade\n para emagrecer.")
        elif (27.3 <= imc <30):#27.8<imc<32
            self.result2["text"]= ("    Acima do peso ideal   \n   IMC= %.1f  " %imc)
            self.pesoideal["text"]=("\n%.1f"%pesoideal) 
            self.recomends["text"]= ("Esta faixa indica que você está com predisposição\n à obesidade; dependendo do seu histórico familiar\n e pessoal, pode haver um quadro de pré-diabetes\n e hipertensão. Procure orientação médica para\n evitar o próximo estágio, Obesidade 1.\n Quanto mais quilos extras, maior a dificuldade\n para emagrecer.")
        elif (30 <= imc <35):#32<imc<38
            self.result2["text"]= ("  Obesidade I\n  IMC= %.1f  " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver diabetes, para quem está \nnesta faixa de peso, é de 20%, e o de hipertensão \nultrapassa 25%. Há risco maior de outras doenças\n cardionvasculares, articulares, distúrbios psiquiá-\ntricos, apneia do sono e até certos tipos de câncer.")
        elif (35 <= imc <40):#38<imc<44
            self.result2["text"]= ("  Obesidade II (Severa)\nIMC= %.1f   " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver diabetes chega a 40%, e a \nchance de surgirem doenças associadas à obesi-\ndade, como reumatismos, câncer, apneia do sono,\n hipertensão e outros problemas cardiovasculares \npode chegar a 50%. Procure orientação médica.")
        elif (imc >= 40):#imc>44
            self.result2["text"]= ("Obesidade III (Mórbida)\nIMC= %.1f" %imc)
            self.result2["fg"]="red"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver doenças associadas ao \nexcesso de peso, como diabetes, reumatismos, \ncâncer, apneia do sono, hipertensão e outros \nproblemas cardiovasculares chega a até 90%. \nNesse estágio, a cirunrgia de redução do \nestômago pode ser indicada.\n Procure orientação médica imediatamente.")

    def mas(self):
        
        peso = float(self.peso.get())
        alt = float(self.altura.get())
        imc = (peso / (alt*alt))
        pesoideal= (((((alt*100)-152.4)/2.54)*1.7)+49)
        popup= Tk()
        popup.title("Resultado")
        popup.geometry("280x280")
        popup.container=Frame(popup)
        popup.container.pack()
        self.result2= Label(popup.container, text="", font="Arial 15 bold")
        self.result2.configure(relief="ridge", border=5, bg= "white")
        self.result2.pack(pady=10)
        self.pesoideal=Label(popup.container, text="", font="Arial 12 bold")
        self.pesoideal.pack(pady=5)
        self.recomends= Label(popup.container, text="")
        self.recomends.pack()
       
        if (imc<19):
            self.result2["text"]= ("   Muito abaixo do peso\n IMC=  %.1f \n   " %imc)
            self.result2["fg"]="red"
            self.pesoideal["text"]=("\n   Seu peso ideal: %.1f   "%pesoideal)                   
            self.recomends["text"]= ("\nNesse ponto, o corpo magro deixa de ser saudável\n e o organismo fica mais vulnerável a infecções. \nSe o baixo peso persistir, mesmo com alimentação\n normal, procure ajuda médica; a dificuldade\n para engordar pode ser sintoma de alguma doença\n insidiosa, como o diabetes.")
        elif (19<imc<20.7):#
            self.result2["text"]= ("   Abaixo do Peso\n  IMC= %.1f   " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\n  Seu peso ideal: %.1f   "%pesoideal) 
            self.recomends["text"]= ("\nNesse ponto, o corpo magro deixa de ser saudável\n e o organismo fica mais vulnerável a infecções. \nSe o baixo peso persistir, mesmo com alimentação\n normal, procure ajuda médica; a dificuldade\n para engordar pode ser sintoma de alguma doença\n insidiosa, como o diabetes.")

        elif (20.7<imc<26.4):
            self.result2["text"]= ("   Peso Normal    \n  IMC= %.1f   " %imc)
            self.pesoideal["text"]=("\n   Seu peso ideal: %.1f   "%pesoideal)
            self.recomends["text"]= ("Seu peso está adequado à altura. É importante\n manter a educação alimentar e a atividade física.\n Fique atento caso seu valor esteja perto dos \nlimites para os estágios de Baixo Peso ou \nSobrepeso.")
        elif (26.4<imc<27.8):
            self.result2["text"]= ("   Marginalmente acima do peso\n IMC= %.1f  " %imc)
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("Esta faixa indica que você está com predisposição\n à obesidade; dependendo do seu histórico familiar\n e pessoal, pode haver um quadro de pré-diabetes\n e hipertensão. Procure orientação médica para\n evitar o próximo estágio, Obesidade 1.\n Quanto mais quilos extras, maior a dificuldade\n para emagrecer.")
        elif (27.8<imc<32):
            self.result2["text"]= ("    Acima do peso ideal   \n   IMC= %.1f  " %imc)
            self.pesoideal["text"]=("Seu peso ideal: \n%.1f"%pesoideal) 
            self.recomends["text"]= ("Esta faixa indica que você está com predisposição\n à obesidade; dependendo do seu histórico familiar\n e pessoal, pode haver um quadro de pré-diabetes\n e hipertensão. Procure orientação médica para\n evitar o próximo estágio, Obesidade 1.\n Quanto mais quilos extras, maior a dificuldade\n para emagrecer.")
        elif (32<imc<38):
            self.result2["text"]= ("  Obesidade I\n  IMC= %.1f  " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver diabetes, para quem está \nnesta faixa de peso, é de 20%, e o de hipertensão \nultrapassa 25%. Há risco maior de outras doenças\n cardionvasculares, articulares, distúrbios psiquiá-\ntricos, apneia do sono e até certos tipos de câncer.")
        elif (38<imc<44):
            self.result2["text"]= ("  Obesidade II (Severa)\nIMC= %.1f   " %imc)
            self.result2["fg"]="orange"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver diabetes chega a 40%, e a \nchance de surgirem doenças associadas à obesi-\ndade, como reumatismos, câncer, apneia do sono,\n hipertensão e outros problemas cardiovasculares \npode chegar a 50%. Procure orientação médica.")
        elif (imc>44):#
            self.result2["text"]= ("Obesidade III (Mórbida)\nIMC= %.1f" %imc)
            self.result2["fg"]="red"
            self.pesoideal["text"]=("\nSeu peso ideal: %.1f"%pesoideal) 
            self.recomends["text"]= ("O risco de desenvolver doenças associadas ao \nexcesso de peso, como diabetes, reumatismos, \ncâncer, apneia do sono, hipertensão e outros \nproblemas cardiovasculares chega a até 90%. \nNesse estágio, a cirunrgia de redução do \nestômago pode ser indicada.\n Procure orientação médica imediatamente.")

    



app(imc)
imc.mainloop()


