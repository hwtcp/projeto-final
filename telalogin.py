from tkinter import *
from tkinter import messagebox
from telaopcoes import Opcoes
from pickle import *

corTela = '#751c1c'
corFundo = '#b9bdbb'

class TelaLogar():
    def __init__(self):

        self.conta = Toplevel()
        self.conta.geometry('1200x1000')
        self.conta.configure(bg=corTela)
        self.conta.title("Login")


        self.frame1 = Frame(self.conta)
        self.frame1["pady"] = 100
        self.frame1.pack()
        self.frame1.configure(bg=corFundo)

        self.titulo = Label(self.frame1, text="LOGIN", bg=corFundo, fg=corTela)
        self.titulo['font'] = ('Saunde', '38')
        self.titulo['pady'] = 30
        self.titulo['padx'] = 1280
        self.titulo.pack()

        self.frameMensagem = Frame(self.conta, pady=50)
        self.frameMensagem.pack()
        self.frameMensagem.configure(bg=corTela)

        self.frame2 = Frame(self.conta)
        self.frame2.pack()
        self.frame2.configure(bg=corTela)

        self.usuariologin = Label(self.frame2, text="Nome de usuário: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo)
        self.usuariologin.pack(side=LEFT)
        self.entradaUsuariologin = Entry(self.frame2, font='ivy, 15')
        self.entradaUsuariologin.pack(side=LEFT)

        self.frame3 = Frame(self.conta)
        self.frame3.pack()
        self.frame3.configure(bg=corTela)
        self.senhalogin = Label(self.frame3, text="Senha: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.senhalogin.pack(side=LEFT)
        self.entradaSenhalogin = Entry(self.frame3, show='*', font='ivy, 15')
        self.entradaSenhalogin.pack(side=LEFT)

        self.frame4 = Frame(self.conta)
        self.frame4.pack()
        self.frame4.configure(bg=corTela)
        self.frame4['pady'] = 50
        self.botao = Button(self.frame4, text='LOGAR', width=10, height=2, font='ivy, 15', bg=corFundo, fg=corTela, command=self.Verifica)
        self.botao.pack()

        self.mensagem = Label(self.frameMensagem, text="", font= 'ivy, 15', fg =corFundo, )
        self.mensagem.configure(bg=corTela)
        self.mensagem.pack()

    def Verifica(self):
        nomelogin = self.entradaUsuariologin.get()
        senhalogin = self.entradaSenhalogin.get()

        if nomelogin == '' or senhalogin == '':
            self.mensagem['text'] = 'Por favor, preencha todos os campos.'
        else:
            try:
                with open("usuarios.txt", "r") as arquivo:
                    for linha in arquivo:
                        nomearquivo, senhaarquivo = linha.strip().split(' | ')
                        if nomearquivo == nomelogin and senhaarquivo == senhalogin:
                            messagebox.showinfo('Show', 'Login realizado com sucesso!')
                            self.conta.destroy()
                            self.abrir_menu()
                            return
                self.mensagem['text'] = 'Ops... Nome de usuário ou senha incorretos.'
            except Exception as e:
                print(f"Erro ao ler o arquivo: {e}")
                self.mensagem['text'] = 'Erro ao ler o arquivo de usuários.'

    def abrir_menu(self):
        Opcoes()