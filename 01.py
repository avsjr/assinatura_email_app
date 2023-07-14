import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Dicionário de opções e imagens correspondentes
opcoes = {
    'Platina CSC': 'img/01-platina.png',
    'Platina LOG': 'img/01-platina.png',
    'Masterline': 'img/02-masterline.png'
}

def selecionar_opcao():
    opcao_selecionada = dropdown.get()
    caminho_imagem = opcoes[opcao_selecionada]
    imagem = Image.open(caminho_imagem)
##  imagem = imagem.resize((500, 197))  # Redimensionar a imagem conforme necessário
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

# Criar a janela principal
janela = tk.Tk()
janela.title('Assinaturas')
janela.geometry('700x700')
janela.configure(bg='white')  # Define a cor de fundo da janela como branco
# Carregar a imagem do ícone e convertê-la para o formato adequado
icone = Image.open('img/skala.png')
icone = icone.resize((32, 32))  # Redimensionar o ícone conforme necessário
icone_tk = ImageTk.PhotoImage(icone)
janela.iconphoto(True, icone_tk) # Definir o ícone da janela

# Criar o dropdown
dropdown = tk.StringVar(janela)
dropdown.set('Escolha a Unidade')  # Opção padrão
opcoes_menu = tk.OptionMenu(janela, dropdown, *opcoes.keys())
opcoes_menu.pack()
opcoes_menu.configure(font=('Arial', 12), fg='black', bg='white')
opcoes_menu['menu'].configure(font=('Arial', 10), fg='black', bg='white')

# Criar a área de texto
##texto = tk.Text(janela, height=10, width=50)
##texto.pack()

# Criar o botão de seleção
botao_selecionar = tk.Button(janela, text='Ok', command=selecionar_opcao)
botao_selecionar.pack()
botao_selecionar.configure(font=('Arial', 12), fg='black', bg='white')
botao_selecionar.place(x=450, y=1)  # Define a posição do botão na janela

# Criar o rótulo para a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
