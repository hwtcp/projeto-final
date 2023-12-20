from tkinter import *
import random

corTela = '#751c1c'
corFundo = '#b9bdbb'

class TlCalculator:
    def __init__(self):
        self.calculator = Toplevel()
        self.calculator.geometry('1280x1024')
        self.calculator.configure(bg = corTela)

        self.frame1 = Frame(self.calculator)
        self.frame1["pady"] = 100
        self.frame1.pack()
        self.frame1.configure(bg=corFundo)

        self.titulo = Label(self.frame1, text="TechLove Calculator", bg=corFundo, fg=corTela)
        self.titulo['font'] = ('Saunde', '38')
        self.titulo['pady'] = 30
        self.titulo['padx'] = 1280
        self.titulo.pack()

        self.frame2 = Frame(self.calculator)
        self.frame2.pack()
        self.frame2.configure(bg=corTela)
        self.nome1 = Label(self.frame2, text="Seu nome: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo)
        self.nome1.pack(side=LEFT)
        self.entryNome1 = Entry(self.frame2, font='ivy, 15')
        self.entryNome1.pack(side=LEFT)

        self.frame3 = Frame(self.calculator)
        self.frame3.pack()
        self.frame3.configure(bg=corTela)
        self.nome2 = Label(self.frame3, text="Nome da pessoa: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.nome2.pack(side=LEFT)
        self.entryNome2 = Entry(self.frame3, font='ivy, 15')
        self.entryNome2.pack(side=LEFT)

        self.frame4 = Frame(self.calculator)
        self.frame4.pack()
        self.frame4.configure(bg=corTela)
        self.frame4['pady'] = 30
        self.botao = Button(self.frame4, text='CALCULAR', width=10, height=2, font='ivy, 15', bg=corFundo, fg=corTela, command=self.result)
        self.botao.pack()

        self.frame5 = Frame(self.calculator)
        self.frame5.pack()
        self.frame5.configure(bg=corTela, pady = 10)
        self.resultado = Label(self.frame5, text=" ", font='ivy, 15', pady = 10, bg=corTela, fg=corFundo)
        self.resultado.pack()

    def result(self):
        x = random.randrange(1,100)
        if x == 0:
            self.resultado["text"] = f"Xiii...{x}% de compatibilidade!"
        if x > 0 and x < 50:
            self.resultado["text"] = f"{x}% de compatibilidade!\nÉ... Melhor que nada"
        if x > 50 and x < 70:
            self.resultado["text"] = f"{x}% de compatibilidade!\nHmm, já é alguma coisa"
        if x > 70:
            self.resultado["text"] = f"{x}% de compatibilidade!\n UAU, deu bom ein!"
        self.botao.destroy
        self.botao2 = Button(self.frame5, text='Tentar novamente', width=30, height=2, font='ivy, 20', bg=corFundo, fg=corTela, command=self.limpar)
        self.botao2.pack()
    
    def limpar(self):
        self.resultado["text"] = ""
        self.entryNome1.delete(0, END) 
        self.entryNome2.delete(0, END)  
        self.botao2.destroy()

