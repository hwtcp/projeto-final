from tkinter import *
from PIL import Image, ImageTk
import os
import pickle

global chats
chats = []

class UsuarioMatch:
  def __init__(self, nome, idade, profissao, imagem, index_chat):
    self.index_chat = index_chat
    self.imagem = imagem
    self.nome = nome
    self.idade = idade
    self.profissao = profissao
    self.__historico = []
    global chats

    if (not os.path.exists("chats")):
      with open("chats", "wb") as arquivo_chats:
        pickle.dump([], arquivo_chats)

    with open("chats", "rb") as arquivo_chats:
      chats = pickle.load(arquivo_chats)
      if index_chat >= len(chats):
        with open("chats", "wb") as arquivo_chats:
          chats.append([])
          print(chats)
          return pickle.dump(chats, arquivo_chats)
      self.set_historico(chats[self.index_chat])
        
  def enviar_mensagem(self):
    valor_entrada = self.entrada.get()
    historico = self.get_historico()
    historico.append(valor_entrada)
    self.set_historico(historico)
    chats[self.index_chat] = historico

    with open("chats", "wb") as arquivo_chats:
      pickle.dump(chats, arquivo_chats)
      self.conversa.destroy()
      self.frame_envio.destroy()
      self.renderizar_conversa()
  
  def get_historico(self):
    return self.__historico

  def set_historico(self, novo_historico):
    self.__historico = novo_historico

  def renderizar_conversa(self):
    contador = 0

    self.conversa = Listbox(self.chat)
    for message in self.get_historico():
      self.conversa.insert(contador, message)
      contador += 1

    self.conversa.pack()

    self.frame_envio = Frame(self.chat)
    self.frame_envio.configure(bg=corTela)
    self.frame_envio.pack()

    self.entrada = Entry(self.frame_envio)
    self.entrada.pack()

    self.botao_enviar = Button(self.frame_envio, text="ENVIAR", bg=corFundo, fg = corTela, command=self.enviar_mensagem)
    self.botao_enviar.pack()
    

  def pegar_chat(self, master):
    self.chat = Toplevel(master=master)
    self.chat.configure(bg=corTela)
    self.chat.geometry("300x400")
    self.renderizar_conversa()

usuarios_match = [
  UsuarioMatch('Olavo Mesquita', '78', 'Médico', 'imagens/0.jpeg', 0),
  UsuarioMatch('Cássio Boll', '34', 'goleiro', 'imagens/1.jpeg', 1),
  UsuarioMatch('Geralda Sousa', '58', 'ex bbb', 'imagens/2.jpeg', 2),
  UsuarioMatch('Priscila Yhusa', '25', 'cantora', 'imagens/3.png', 3),
  UsuarioMatch('Paulo Osvaldo', '45', 'Ator', 'imagens/4.jpg', 4),
]

corTela = '#751c1c'
corFundo = '#b9bdbb'

class TelaMatch(Toplevel):
  def __init__(self):
    super().__init__()
    self.geometry('600x600')
    self.configure(bg=corTela)
    self.minsize(260, 500)
    self.configure(bg=corTela)
    self.usuario_atual = 0
    self.renderizar()

  def renderizar(self):
    self.image_atual = usuarios_match[self.usuario_atual].imagem
    self.nome_usuario = usuarios_match[self.usuario_atual].nome
    self.idade_usuario = usuarios_match[self.usuario_atual].idade
    self.profissao_usuario = usuarios_match[self.usuario_atual].profissao
    
    self.label_nome_usuario = Label(self, text=f'{self.nome_usuario}, {self.idade_usuario} anos, {self.profissao_usuario}', bg=corFundo, fg = corTela, font='ivy, 15')
    self.label_nome_usuario.pack()

    self.frame_usuario = Frame(self, width=240)
    self.frame_usuario.pack()

    self.imagem_usuario = ImageTk.PhotoImage(Image.open(self.image_atual).resize((240, 420)))
    
    self.label_imagem_usuario = Label(self.frame_usuario, image=self.imagem_usuario)
    self.label_imagem_usuario.pack()

    self.botao_match = Button(self.frame_usuario, text="MATCH", bg=corFundo, fg=corTela, command=self.match)
    self.botao_match.pack(side=LEFT)
    self.botao_match['pady'] = 10
    self.botao_match['padx'] = 40

    self.botao_proximo = Button(self.frame_usuario, text="PRÓXIMO", bg=corFundo, fg=corTela, command=self.pegar_proximo)
    self.botao_proximo.pack(side=RIGHT)
    self.botao_proximo['pady'] = 10
    self.botao_proximo['padx'] = 40

  def pegar_proximo(self):
    self.usuario_atual += 1
    if (len(usuarios_match) <= self.usuario_atual): return
    self.frame_usuario.destroy()
    self.label_nome_usuario.destroy()
    self.renderizar()

  def match(self):
    usuarios_match[self.usuario_atual].pegar_chat(self.master)
    self.usuario_atual