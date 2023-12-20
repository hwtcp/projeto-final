import os
from tkinter import *
from tkinter import messagebox

corTela = '#751c1c'
corFundo = '#b9bdbb'

class TelaCriar():
    def __init__(self, nomedoarquivo):
        self.nomedoarquivo = nomedoarquivo
        self.conta = Toplevel()
        self.conta.geometry('1280x1024')
        self.conta.configure(bg=corTela)
        self.conta.title("Janela 2")

        self.frame1 = Frame(self.conta)
        self.frame1["pady"] = 100
        self.frame1.pack()
        self.frame1.configure(bg=corFundo)

        self.titulo = Label(self.frame1, text="CRIAR CONTA", bg=corFundo, fg=corTela)
        self.titulo['font'] = ('Saunde', '38')
        self.titulo['pady'] = 30
        self.titulo['padx'] = 1280
        self.titulo.pack()

        self.frame2 = Frame(self.conta, pady=50)
        self.frame2.pack()
        self.frame2.configure(bg=corTela)
        self.nome = Label(self.frame2, text="Como você se chama?  ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo)
        self.nome.pack(side=LEFT)
        self.entradaNome = Entry(self.frame2, width='30', font='ivy, 15')
        self.entradaNome.pack(side=LEFT)

        self.frame3 = Frame(self.conta)
        self.frame3.pack()
        self.frame3.configure(bg=corTela)
        self.nome_usuario = Label(self.frame3, text="Nome de usuário: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo)
        self.nome_usuario.pack(side=LEFT)
        self.entradaNome_usuario = Entry(self.frame3, width='30', font='ivy, 15')
        self.entradaNome_usuario.pack(side=LEFT)

        self.frame4 = Frame(self.conta)
        self.frame4.pack()
        self.frame4.configure(bg=corTela)
        self.senha = Label(self.frame4, text="Senha: ", pady=5,  font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.senha.pack(side=LEFT)
        self.entradaSenha = Entry(self.frame4, show='*', width='30', font='ivy, 15')
        self.entradaSenha.pack(side=LEFT)

        self.frame5 = Frame(self.conta)
        self.frame5.pack()
        self.frame5.configure(bg=corTela)
        self.frame5['pady'] = 50
        self.botao_confirmar = Button(self.frame5, text='CRIAR', width=10, height=2, font='ivy, 15', bg=corFundo, fg=corTela, command=self.registrar_usuario)
        self.botao_confirmar.pack()

        self.mensagem = Label(self.frame5, text="", font= 'ivy, 15', fg =corFundo, )
        self.mensagem.configure(bg=corTela)
        self.mensagem.pack()

    def registrar_usuario(self):
        nome = self.entradaNome.get()
        nome_usuario = self.entradaNome_usuario.get()
        senha = self.entradaSenha.get()

        if nome == '' or nome_usuario == '' or senha == '':
            messagebox.showinfo('ei', 'Por favor, preencha todos os campos.')
            return

        if len(senha) < 8:
            self.mensagem['text'] = 'Por favor, crie uma senha com pelo menos 8 caracteres.'
            return

        if not os.path.exists("usuarios.txt"):
            open("usuarios.txt", "a").close()

        try:
            with open('usuarios.txt', 'r') as file:
                for linha in file:
                    nomearquivo, _ = linha.strip().split(' | ')
                    if nomearquivo == nome_usuario:
                        self.mensagem['text'] = 'Esse nome de usuário já existe.'
                        return

                with open('usuarios.txt', 'a') as arquivo_escrita:
                    arquivo_escrita.write(f"{nome_usuario} | {senha}\n")
                    messagebox.showinfo(f'Olá, {nome}!', 'Sua conta foi criada com sucesso.')

        except Exception as e:
            print(f"Erro: {e}")