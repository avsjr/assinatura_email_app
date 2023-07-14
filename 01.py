import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont

# Dicionário de opções e imagens correspondentes
opcoes = {
    'Platina CSC': 'img/01-platina.png',
    'Platina LOG': 'img/01-platina.png',
    'Masterline': 'img/02-masterline.png'
}

# Função para selecionar a opção do dropdown
def selecionar_opcao():
    opcao_selecionada = dropdown.get()
    caminho_imagem = opcoes[opcao_selecionada]
    imagem = Image.open(caminho_imagem)
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

# Criar a janela principal
janela = tk.Tk()
janela.title('Assinaturas')    # Define o título da janela
janela.geometry('700x700')     # Define o tamanho da janela
janela.configure(bg='white')   # Define a cor de fundo da janela como branco

# Carregar a imagem do ícone e convertê-la para o formato adequado
icone = Image.open('img/skala.png')
icone = icone.resize((32, 32))       # Redimensionar o ícone conforme necessário
icone_tk = ImageTk.PhotoImage(icone) # Converter o ícone para o formato do tkinter
janela.iconphoto(True, icone_tk)     # Definir o ícone da janela

# Criar o dropdown
dropdown = tk.StringVar(janela)    # Variável para armazenar a opção selecionada
dropdown.set('Escolha a Unidade')  # Opção padrão

# Criar o dropdown com as opções
opcoes_menu = tk.OptionMenu(janela, dropdown, *opcoes.keys())

# Definir as propriedades do dropdown
opcoes_menu.pack(side='top', padx=10, pady=10)
opcoes_menu.configure(
    font=('Arial', 12),   # Define a fonte
    fg='black',           # Define a cor do texto
    bg='white',           # Define a cor de fundo
    relief='flat',        # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=15              # Define a largura do dropdown em caracteres
)

# Definir as propriedades do menu suspenso
opcoes_menu['menu'].configure(
    font=('Arial', 12),   # Define a fonte do menu suspenso
    fg='black',           # Define a cor do texto no menu suspenso
    bg='white',           # Define a cor de fundo do menu suspenso
    relief='flat',        # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
)

'''
# Criar a área de texto
texto = tk.Text(janela, height=10, width=50)
texto.pack()
'''

# Criar o botão de seleção
botao_selecionar = tk.Button(janela, text='Ok', command=selecionar_opcao)
#botao_selecionar.pack(side='top', padx=0, pady=0)
botao_selecionar.place(x=450, y=11)  # Define a posição do botão na janela
botao_selecionar.configure(          # Define as propriedades do botão
    font=('Arial', 12),              # Define a fonte
    fg='black',                      # Define a cor do texto
    bg='white',                      # Define a cor de fundo
    relief='flat',                   # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=2                          # Define a largura do dropdown em caracteres
)

# Criar o campo de entrada de texto
campo_texto = tk.Entry(janela, font=('Arial', 12), width=30)
campo_texto.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada


def adicionar_texto():
    texto_inserido = campo_texto.get()  # Obter o texto inserido pelo usuário

    # Carregar a imagem
    caminho_imagem = opcoes[dropdown.get()]  # Obter o caminho da imagem selecionada
    imagem = Image.open(caminho_imagem)

    # Criar uma instância de ImageDraw para desenhar na imagem
    desenho = ImageDraw.Draw(imagem)

    # Definir o texto a ser adicionado
    texto = texto_inserido

    # Definir a fonte e o tamanho do texto
    tamanho_fonte = 30
    fonte = ImageFont.truetype('fonts/arial.ttf', tamanho_fonte)

    # Definir a posição do texto na imagem
    posicao_texto = (50, 50)  # exemplo: posição (50, 50)

    # Definir a cor do texto
    cor_texto = (69,139,116)  # exemplo: branco (RGB)

    # Desenhar o texto na imagem
    desenho.text(posicao_texto, texto, font=fonte, fill=cor_texto)

    # Atualizar a imagem exibida no rótulo label_imagem
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

# Criar o botão para adicionar o texto
botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar_texto)
botao_adicionar.pack(pady=10)


#### Criar botão nova assinatura
# Criar o rótulo para a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
