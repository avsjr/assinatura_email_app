import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageOps

# Dicionário de opções e imagens correspondentes
opcoes = {
    'Platina CSC': 'img/02-platina.png',
    'Platina LOG': 'img/02-platina.png',
    'Masterline': 'img/01-masterline.png'
}

# Função para selecionar a opção do dropdown
def selecionar_opcao():
    global imagem
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
# Adicionar uma borda ao ícone
borda_size = 2  # Tamanho da borda em pixels
borda_cor = (162,205,90)  # Cor da borda (vermelho no exemplo)
icone_com_borda = ImageOps.expand(icone, border=borda_size, fill=borda_cor)

# Converter o ícone para o formato do tkinter
icone_tk = ImageTk.PhotoImage(icone_com_borda)
janela.iconphoto(True, icone_tk)     # Definir o ícone da janela

# Criar o dropdown
dropdown = tk.StringVar(janela)    # Variável para armazenar a opção selecionada
dropdown.set('Escolha a Unidade')  # Opção padrão

# Criar o dropdown com as opções
opcoes_menu = tk.OptionMenu(janela, dropdown, *opcoes.keys())

# Definir as propriedades do dropdown
opcoes_menu.pack(side='top', padx=7, pady=7)
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

# Criar o botão de seleção
botao_selecionar = tk.Button(janela, text='OK', command=selecionar_opcao)
#botao_selecionar.pack(side='top', padx=0, pady=0)
botao_selecionar.place(x=450, y=8)  # Define a posição do botão na janela
botao_selecionar.configure(          # Define as propriedades do botão
    font=('Arial', 12),              # Define a fonte
    fg='black',                      # Define a cor do texto
    bg='white',                      # Define a cor de fundo
    relief='flat',                   # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=2                          # Define a largura do dropdown em caracteres
)

# Criar o campo de entrada de texto
rotulo_instrucao = tk.Label(janela, text="Nome", font=('Arial', 11), bg="white")
rotulo_instrucao.pack()
campo_nome = tk.Entry(janela, font=('Arial', 12), width=30)
campo_nome.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="Cargo", font=('Arial', 11), bg="white")
rotulo_instrucao.pack()
campo_cargo = tk.Entry(janela, font=('Arial', 12), width=30)
campo_cargo.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="E-mail", font=('Arial', 11), bg="white")
rotulo_instrucao.pack()
campo_email = tk.Entry(janela, font=('Arial', 12), width=30)
campo_email.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="Telefone", font=('Arial', 11), bg="white")
rotulo_instrucao.pack()
campo_telefone = tk.Entry(janela, font=('Arial', 12), width=30)
campo_telefone.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

def adicionar_texto():
    texto_inserido_nome = campo_nome.get()  # Obter o texto inserido pelo usuário
    texto_inserido_cargo = campo_cargo.get()
    texto_inserido_email = campo_email.get()
    texto_inserido_telefone = campo_telefone.get()
    
    # Carregar a imagem
    caminho_imagem = opcoes[dropdown.get()]  # Obter o caminho da imagem selecionada
    imagem = Image.open(caminho_imagem)
    
    desenho = ImageDraw.Draw(imagem) # Criar uma instância de ImageDraw para desenhar na imagem
    #desenho_endereco = ImageDraw.Draw(imagem)
    
    # Definir o texto a ser adicionado
    texto_nome = texto_inserido_nome
    texto_cargo = texto_inserido_cargo
    texto_email = texto_inserido_email
    texto_telefone = texto_inserido_telefone
    endereco_platina = 'Comercial Ilhas do Sol\nRua Coronel Antonio Rios, 1097 - Salas 201 a 208\nUberaba/MG'
    endereco_masterline = 'Rua Verissímo, 265\nSão Benedito - Uberaba/MG\nCEP: 38020-310'
    
    # Definir a fonte e o tamanho do texto
    tamanho_fonte = 15
    
    fonte_atributos = ImageFont.truetype('fonts/arial.ttf', tamanho_fonte)
    fonte_endereco = ImageFont.truetype('fonts/arial.ttf', tamanho_fonte,)
    
    # Definir a cor do texto
    cor_nome_cargo = (162,205,90)
    cor_email_telefone = (3,3,3)
    cor_endereco = (3,3,3)
    
    if caminho_imagem == 'img/01-masterline.png':
        posicao_endereco = (210, 126)  # Definir a posição do endereço masterline
        desenho.text(posicao_endereco, endereco_masterline, font=fonte_endereco, fill=cor_endereco)
        
    else:
        posicao_endereco = (192, 126)  # Definir a posição do endereço platina
        desenho.text(posicao_endereco, endereco_platina, font=fonte_endereco, fill=cor_endereco)
          
    # condição para a posição do texto
    if caminho_imagem == 'img/01-masterline.png':
        posicao_nome = (210, 18)  # Definir a posição do texto na imagem
        desenho.text(posicao_nome, texto_nome, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_cargo = (210, 38)  # Definir a posição do texto na imagem
        desenho.text(posicao_cargo, texto_cargo, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_email = (210, 58)  # Definir a posição do texto na imagem
        desenho.text(posicao_email, texto_email, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone = (210, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone, texto_telefone, font=fonte_atributos, fill=cor_email_telefone)
    else:
        posicao_nome = (192, 18)  # Definir a posição do texto na imagem
        desenho.text(posicao_nome, texto_nome, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_cargo = (192, 38)  # Definir a posição do texto na imagem
        desenho.text(posicao_cargo, texto_cargo, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_email = (192, 58)  # Definir a posição do texto na imagem
        desenho.text(posicao_email, texto_email, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone = (192, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone, texto_telefone, font=fonte_atributos, fill=cor_email_telefone)

    # Atualizar a imagem exibida no rótulo label_imagem
    
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk
    
           
# Criar o botão para adicionar o texto
botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar_texto)
botao_adicionar.pack(pady=10)
botao_adicionar.configure(          # Define as propriedades do botão
    font=('Arial', 12),              # Define a fonte
    fg='black',                      # Define a cor do texto
    bg='white',                      # Define a cor de fundo
    relief='flat',                   # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=6                          # Define a largura do dropdown em caracteres
)    


def salvar_imagem():
        global contador, imagem
        # Converter a imagem para o modo RGB
        imagem = imagem.convert("RGB")
        
        # Abrir o diálogo de seleção de diretório
        diretorio = filedialog.asksaveasfilename(defaultextension=".jpg")
    
        if diretorio:
        # Salvar a imagem modificada no diretório selecionado
            imagem.save(diretorio)
            print("Imagem salva com sucesso!")

# Criar botão salvar imagem
botao_salvar = tk.Button(janela, text="Salvar Imagem", command=salvar_imagem)
botao_salvar.pack(side='bottom',padx=7, pady=7)
botao_salvar.configure(
    font=('Arial', 12),   # Define a fonte
    fg='black',           # Define a cor do texto
    bg='white',           # Define a cor de fundo
    relief='flat',        # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=10              # Define a largura do dropdown em caracteres)
) 

#Criar botão nova assinatura

# Criar o rótulo para a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
