from tkinter import *
from telaopcao1 import CriarPerfil
from telaopcao2 import TlCalculator
from telamatch import TelaMatch

corTela = '#751c1c'
corFundo = '#b9bdbb'

class Opcoes:
    def __init__(self):
        self.opcoes = Toplevel()
        self.opcoes.geometry('600x500')
        self.opcoes.configure(bg=corFundo)
        self.opcoes.title('opções')

        self.frame1 = Frame(self.opcoes, bg=corFundo)
        self.frame1['pady']=30
        self.frame1.pack()
        self.frame2 = Frame(self.opcoes, bg=corFundo)
        self.frame2['pady']=30
        self.frame2.pack()
        self.frame3 = Frame(self.opcoes, bg=corFundo)
        self.frame3['pady']=30
        self.frame3.pack()

        self.botao_perfil = Button(self.frame1, text='FAÇA SEU PERFIL', width=20, height=2, font='ivy, 20', bg=corTela, fg=corFundo, padx=28, command=self.opcao1)
        self.botao_perfil.pack()
        self.botao_calculator = Button(self.frame2, text='CALCULATOR', width=15, height=2, font='ivy, 20', padx=24, bg=corTela, fg=corFundo, command =self.opcao2)
        self.botao_calculator.pack()
        self.botao_catalogo = Button(self.frame3, text='CATÁLOGO', width=12, height=2, font='ivy, 20', padx=20, bg=corTela, fg=corFundo, command = self.opcao3)
        self.botao_catalogo.pack()

    def opcao1(self):
        CriarPerfil()

    def opcao2(self):
        TlCalculator()

    def opcao3(self):
        TelaMatch()