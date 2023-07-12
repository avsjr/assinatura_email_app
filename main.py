# Trabalhar com imagens
from PIL import Image
# Desenhar na imagem
from PIL import ImageDraw
# Escolher a fonte do texto
from PIL import ImageFont

from tkinter import *


# escolher qual unidade de negócio
unidades = ['Masterline', 'Platina Log', 'Platina CSC']
user_input = ''
unidade_negocio = "Escolha a unidade do Grupo Skala"


# Quais palavras colocar
palavras = ['Antonio Vicente']

contador = 1
for palavra in palavras:
    # váriavel para abrir imagem
    imagem = Image.open('assinatura.jpg')
    # abir a imagem para edição
    draw = ImageDraw.Draw(imagem)
    # escolher fonte
    font = ImageFont.truetype('arial.ttf',15)
    draw.text((215,29),palavra,fill =(0,0,0),font=font,)
    # salvar a imagem modificada
    imagem.save(f'imagem{contador}.jpg')
    contador += 1
    