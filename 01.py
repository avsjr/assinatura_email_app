import tkinter as tk
from PIL import Image, ImageTk

# Dicionário de opções e imagens correspondentes
opcoes = {
    'Opção 1': 'caminho/para/imagem1.jpg',
    'Opção 2': 'caminho/para/imagem2.jpg',
    'Opção 3': 'caminho/para/imagem3.jpg'
}

def selecionar_opcao():
    opcao_selecionada = dropdown.get()
    caminho_imagem = opcoes[opcao_selecionada]
    imagem = Image.open(caminho_imagem)
    imagem = imagem.resize((300, 300))  # Redimensionar a imagem conforme necessário
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk

# Criar a janela principal
janela = tk.Tk()
janela.title('App com Dropdown')

# Criar o dropdown
dropdown = tk.StringVar(janela)
dropdown.set('Opção 1')  # Opção padrão

opcoes_menu = tk.OptionMenu(janela, dropdown, *opcoes.keys())
opcoes_menu.pack()

# Criar a área de texto
texto = tk.Text(janela, height=10, width=50)
texto.pack()

# Criar o botão de seleção
botao_selecionar = tk.Button(janela, text='Selecionar', command=selecionar_opcao)
botao_selecionar.pack()

# Criar o rótulo para a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
