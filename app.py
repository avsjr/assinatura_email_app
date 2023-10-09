import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont, ImageOps

# Definição de constantes
IMG_ML = 'img/01-masterline.png'
IMG_PL = 'img/02-platina.png'

# Dicionário de opções e imagens correspondentes
opcoes = {
    'Platina CSC': IMG_PL,
    'Platina LOG': IMG_PL,
    'Masterline': IMG_ML
}

# Função para selecionar a opção do dropdown
def selecionar_opcao(*args):
    global imagem
    opcao_selecionada = dropdown.get()
    caminho_imagem = opcoes[opcao_selecionada]
    imagem = Image.open(caminho_imagem)
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk
    
    if caminho_imagem == IMG_ML:
        campo_email.insert(0, '@masterline.ind.br')
    else:
        campo_email.insert(0, '@platinacsc.com.br')
    
# Criar a janela principal
janela = tk.Tk()
janela.title('Assinaturas')
janela.geometry('800x800')
janela.configure(bg='white')
janela.iconbitmap('img/skala.ico')  # Define o ícone da janela

# Carregar a imagem do ícone e convertê-la para o formato adequado
icone = Image.open('img/skala.ico')
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
    font=('Arial', 10),   # Define a fonte
    fg='black',           # Define a cor do texto
    bg='white',           # Define a cor de fundo
    relief='ridge',        # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=15,              # Define a largura do dropdown em caracteres
    bd=1
)

# Definir as propriedades do menu suspenso
opcoes_menu['menu'].configure(
    font=('Arial', 10),   # Define a fonte do menu suspenso
    fg='black',           # Define a cor do texto no menu suspenso
    bg='white',           # Define a cor de fundo do menu suspenso
    relief='ridge',        # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
)

# Associar a função selecionar_opcao() ao evento de mudança da variável do dropdown
dropdown.trace("w", selecionar_opcao)

# Criar o campo de entrada de texto
rotulo_instrucao = tk.Label(janela, text="Nome", font=('Arial', 10), bg="white")
rotulo_instrucao.pack()
campo_nome = tk.Entry(janela, font=('Arial', 11), width=40, bg='white', fg='black', bd=1, relief='ridge')
campo_nome.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="Cargo", font=('Arial', 10), bg="white")
rotulo_instrucao.pack()
campo_cargo = tk.Entry(janela, font=('Arial', 11), width=40, bg='white', fg='black', bd=1, relief='ridge')
campo_cargo.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="Email", font=('Arial', 10), bg="white")
rotulo_instrucao.pack()
campo_email = tk.Entry(janela, font=('Arial', 11), width=40, bg='white', fg='black', bd=1, relief='ridge')
campo_email.pack(pady=10)  # Adicionar preenchimento vertical ao campo de entrada

rotulo_instrucao = tk.Label(janela, text="Telefone Fixo", font=('Arial', 10), bg="white")
rotulo_instrucao.pack()
campo_telefone_fixo = tk.Entry(janela, font=('Arial', 11), width=40, bg='white', fg='black', bd=1, relief='ridge')
campo_telefone_fixo.pack(pady=10)

rotulo_instrucao = tk.Label(janela, text="Telefone Móvel (opcional)", font=('Arial', 10), bg="white")
rotulo_instrucao.pack()
campo_telefone_movel = tk.Entry(janela, font=('Arial', 11), width=40, bg='white', fg='black', bd=1, relief='ridge')
campo_telefone_movel.pack(pady=10)

def adicionar_texto():
    global imagem_modificada
    texto_inserido_nome = campo_nome.get()  # Obter o texto inserido pelo usuário
    texto_inserido_cargo = campo_cargo.get()
    texto_inserido_email = campo_email.get()
    texto_inserido_telefone_fixo = campo_telefone_fixo.get()
    texto_inserido_telefone_movel = campo_telefone_movel.get()
    
    # Carregar a imagem
    caminho_imagem = opcoes[dropdown.get()]  # Obter o caminho da imagem selecionada
    imagem = Image.open(caminho_imagem)
    
    desenho = ImageDraw.Draw(imagem) # Criar uma instância de ImageDraw para desenhar na imagem
    #desenho_endereco = ImageDraw.Draw(imagem)
    
    # Definir o texto a ser adicionado
    texto_nome = texto_inserido_nome
    texto_cargo = texto_inserido_cargo
    texto_email = texto_inserido_email
    texto_telefone_fixo = texto_inserido_telefone_fixo
    texto_telefone_movel = texto_inserido_telefone_movel
    endereco_platina = 'Comercial Ilhas do Sol\nRua Coronel Antonio Rios, 1097 - Salas 201 a 208\nUberaba/MG'
    endereco_masterline = 'Rua Verissímo, 265\nSão Benedito - Uberaba/MG\nCEP: 38020-310'
    
    # Definir a fonte e o tamanho do texto
    tamanho_fonte = 15
    
    fonte_atributos = ImageFont.truetype('fonts/josefins/JosefinSans-Regular.ttf', tamanho_fonte)
    fonte_endereco = ImageFont.truetype('fonts/josefins/JosefinSans-Regular.ttf', tamanho_fonte,)
    
    # Definir a cor do texto
    cor_nome_cargo = (162,205,90)
    cor_email_telefone = (3,3,3)
    cor_endereco = (3,3,3)
    
    if caminho_imagem == IMG_ML:
        posicao_endereco = (203, 126)  # Definir a posição do endereço masterline
        desenho.text(posicao_endereco, endereco_masterline, font=fonte_endereco, fill=cor_endereco)
        
    else:
        posicao_endereco = (185, 126)  # Definir a posição do endereço platina
        desenho.text(posicao_endereco, endereco_platina, font=fonte_endereco, fill=cor_endereco)
        campo_email.insert(0, '@platinacsc.com.br')
          
    # condição para a posição do texto
    if caminho_imagem == IMG_ML:
        posicao_nome = (210, 18)  # Definir a posição do texto na imagem
        desenho.text(posicao_nome, texto_nome, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_cargo = (210, 38)  # Definir a posição do texto na imagem
        desenho.text(posicao_cargo, texto_cargo, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_email = (210, 58)  # Definir a posição do texto na imagem
        desenho.text(posicao_email, texto_email, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone_fixo = (210, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone_fixo, texto_telefone_fixo, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone_movel = (350, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone_movel, texto_telefone_movel, font=fonte_atributos, fill=cor_email_telefone)
    else:
        posicao_nome = (192, 18)  # Definir a posição do texto na imagem
        desenho.text(posicao_nome, texto_nome, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_cargo = (192, 38)  # Definir a posição do texto na imagem
        desenho.text(posicao_cargo, texto_cargo, font=fonte_atributos, fill=cor_nome_cargo)
        posicao_email = (192, 58)  # Definir a posição do texto na imagem
        desenho.text(posicao_email, texto_email, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone_fixo = (192, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone_fixo, texto_telefone_fixo, font=fonte_atributos, fill=cor_email_telefone)
        posicao_telefone_movel = (330, 78)  # Definir a posição do texto na imagem
        desenho.text(posicao_telefone_movel, texto_telefone_movel, font=fonte_atributos, fill=cor_email_telefone)

    # Atualizar a imagem exibida no rótulo label_imagem
    
    imagem_tk = ImageTk.PhotoImage(imagem)
    label_imagem.configure(image=imagem_tk)
    label_imagem.image = imagem_tk
    
    # Atualizar a imagem modificada
    imagem_modificada = imagem
    
           
# Criar o botão para adicionar o texto
botao_adicionar = tk.Button(janela, text='Adicionar', command=adicionar_texto)
botao_adicionar.pack(pady=10)
botao_adicionar.configure(          # Define as propriedades do botão
    font=('Arial', 10),              # Define a fonte
    fg='black',                      # Define a cor do texto
    bg='white',                      # Define a cor de fundo
    relief='ridge',                   # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=8                          # Define a largura do dropdown em caracteres
)    

# Função para limpar todos os campos
def limpar_campos():
    campo_nome.delete(0, 'end')  # Limpa o campo de Nome
    campo_cargo.delete(0, 'end')  # Limpa o campo de Cargo
    campo_email.delete(0, 'end')  # Limpa o campo de Email
    campo_telefone_fixo.delete(0, 'end')  # Limpa o campo de Telefone Fixo
    campo_telefone_movel.delete(0, 'end')  # Limpa o campo de Telefone Móvel
    dropdown.set('Escolha a Unidade')  # Define a opção padrão no dropdown

# Criar o botão para limpar todos os campos
botao_limpar = tk.Button(janela, text='Limpar Campos', command=limpar_campos)
botao_limpar.pack(pady=10)
botao_limpar.configure(          # Define as propriedades do botão
    font=('Arial', 10),              # Define a fonte
    fg='black',                      # Define a cor do texto
    bg='white',                      # Define a cor de fundo
    relief='ridge',                   # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=11                          # Define a largura do botão em caracteres
)

def salvar_imagem():
    global imagem_modificada
    if imagem_modificada:
        # Converta a imagem para o modo RGB, se necessário
        imagem_salvar = imagem_modificada.convert("RGB")

        # Abrir o diálogo de seleção de diretório
        diretorio = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG", ".jpeg"), ("PNG", ".png")], title="Salvar Imagem")

        if diretorio:
            # Salvar a imagem modificada no diretório selecionado
            imagem_salvar.save(diretorio)
            # Exibir mensagem de sucesso ao usuário
            messagebox.showinfo("Sucesso", "Imagem salva com sucesso!")

# Criar botão salvar imagem
botao_salvar = tk.Button(janela, text="Salvar Imagem", command=salvar_imagem)
botao_salvar.pack(side='bottom',padx=7, pady=7)
botao_salvar.configure(
    font=('Arial', 10),   # Define a fonte
    fg='black',           # Define a cor do texto
    bg='white',           # Define a cor de fundo
    relief='ridge',       # Define o estilo de borda (por exemplo, 'flat', 'raised', 'sunken')
    width=11              # Define a largura do dropdown em caracteres)
) 

# Criar o rótulo para a imagem
label_imagem = tk.Label(janela)
label_imagem.pack()

janela.mainloop()
