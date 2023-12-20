from tkinter import *
from telacriar import TelaCriar
from telalogin import TelaLogar

corTela = '#751c1c'
corFundo = '#b9bdbb'

class Menu:
    def __init__(self, mestre):
        self.mestre = mestre
        
        self.frame1=Frame(mestre, width=1280, height=300)
        self.frame1.configure(bg=corFundo)
        self.frame1['pady']=100
        self.frame1.pack()

        self.texto1 = Label(self.frame1, text='TechLove:\nConectando destinos', font='finish, 38', bg=corFundo, fg=corTela)
        self.texto1.pack()
        self.texto1['pady']=30
        self.texto1['padx']=1280

        self.frame2 = Frame(mestre, bg=corTela)
        self.frame2['pady']=100
        self.frame2.pack()

        self.botao_cadastro = Button(self.frame2, text='CRIAR CONTA', width=15, height=2, font='ivy, 20', bg=corFundo, fg=corTela, padx=80, command=self.Criar)
        self.botao_cadastro.pack()
        self.entrar=Label(self.frame2, text='Já possui uma conta?', font='newspaper, 15', bg=corTela, fg='white', pady=20)
        self.entrar.pack()
        self.botao_login = Button(self.frame2, text='ENTRAR', width=15, height=2, font='ivy, 20', padx=20, bg=corFundo, fg=corTela, command=self.Login)
        self.botao_login.pack()

    def Criar(self):
        TelaCriar('usuarios.txt')

    def Login(self):
        TelaLogar()
             
raiz = Tk()
Menu(raiz)
raiz.configure(bg=corTela)
raiz.geometry('1280x1024')
raiz.mainloop()
