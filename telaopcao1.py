from tkinter import *

corTela = '#751c1c'
corFundo = '#b9bdbb'

class CriarPerfil:
    def __init__(self):
        self.perfil = Toplevel()
        self.perfil.geometry('1280x1024')
        self.perfil.configure(bg=corTela)
        self.perfil.title("criar perfil")


        self.frame1 = Frame(self.perfil)
        self.frame1["pady"] = 100
        self.frame1.pack()
        self.frame1.configure(bg=corFundo)

        self.titulo = Label(self.frame1, text="CRIE SEU PERFIL", bg=corFundo, fg=corTela)
        self.titulo['font'] = ('Saunde', '38')
        self.titulo['pady'] = 30
        self.titulo['padx'] = 1280
        self.titulo.pack()

        self.frame2 = Frame(self.perfil)
        self.frame2.pack()
        self.frame2.configure(bg=corTela)
        self.nome = Label(self.frame2, text="Nome: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo)
        self.nome.pack(side=LEFT)
        self.entryNome = Entry(self.frame2, font='ivy, 15')
        self.entryNome.pack(side=LEFT)

        self.frame3 = Frame(self.perfil)
        self.frame3.pack()
        self.frame3.configure(bg=corTela)
        self.idade = Label(self.frame3, text="Idade: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.idade.pack(side=LEFT)
        self.entryIdade = Entry(self.frame3, font='ivy, 15')
        self.entryIdade.pack(side=LEFT)

        self.frame4 = Frame(self.perfil)
        self.frame4.pack()
        self.frame4.configure(bg=corTela)
        self.sexo = Label(self.frame4, text="Sexo: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.sexo.pack(side=LEFT)
        self.entrySexo = Entry(self.frame4, font='ivy, 15')
        self.entrySexo.pack(side=LEFT)

        self.frame5 = Frame(self.perfil)
        self.frame5.pack()
        self.frame5.configure(bg=corTela)
        self.profissao = Label(self.frame5, text="Profissão: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.profissao.pack(side=LEFT)
        self.entryProfissao = Entry(self.frame5, font='ivy, 15')
        self.entryProfissao.pack(side=LEFT)

        self.frame6 = Frame(self.perfil)
        self.frame6.pack()
        self.frame6.configure(bg=corTela)
        self.cidade = Label(self.frame6, text="Cidade: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.cidade.pack(side=LEFT)
        self.entryCidade = Entry(self.frame6, font='ivy, 15')
        self.entryCidade.pack(side=LEFT)

        self.frame7 = Frame(self.perfil)
        self.frame7.pack()
        self.frame7.configure(bg=corTela)
        self.recado = Label(self.frame7, text="Recado: ", pady=5, font='ivy, 20', bg=corTela, fg=corFundo, anchor='ne')
        self.recado.pack(side=LEFT)
        self.entryRecado = Entry(self.frame7, font='ivy, 15')
        self.entryRecado.pack(side=LEFT)

        self.frame8 = Frame(self.perfil)
        self.frame8.pack()
        self.frame8.configure(bg=corTela)
        self.frame8['pady'] = 50
        self.botao_criar = Button(self.frame8, text='Criar', width=10, height=2, font='ivy, 15', bg=corFundo, fg=corTela, command = self.salvar_perfil)
        self.botao_criar.pack()
        self.botao_editar = Button(self.frame8, text='Editar', width=10, height=2, font='ivy, 15', bg=corFundo, fg=corTela, command = self.salvar_perfil)
        self.botao_editar.pack()

        self.mensagem = Label(self.frame9, text="", font= 'ivy, 15', fg =corFundo, )
        self.mensagem.configure(bg=corTela)
        self.mensagem.pack()

        self.frame9 = Frame(self.perfil)
        self.frame9.pack()
        self.frame9.configure(bg=corTela)
        self.frame9['pady'] = 7

    def salvar_perfil(self):
        nome = self.entryNome.get()
        idade = self.entryIdade.get()
        sexo = self.entrySexo.get()
        profissao = self.entryProfissao.get()
        cidade = self.entryCidade.get()
        recado = self.entryRecado.get()

        perfil_texto = f"Nome: {nome}\nIdade: {idade}\nSexo: {sexo}\nProfissão: {profissao}\nCidade: {cidade}\nRecado: {recado}"

        try:
            with open("perfil_usuario.txt", "w") as arquivo:
                arquivo.write(perfil_texto)
            self.mensagem["text"] = "Perfil criado!"
        except Exception as e:
            self.mensagem["text"] = f"Erro ao salvar o perfil: {e}"

    def editarperfil(self):
        self.entryNome.delete(0, END)
        self.entryIdade.delete(0, END)
        self.entrySexo.delete(0, END)
        self.entryProfissao.delete(0, END)
        self.entryCidade.delete(0, END)
        self.entryRecado.delete(0, END)
        self.mensagem['text'] = ''




        
    
