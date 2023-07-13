import tkinter as tk

# Crie uma janela principal
window = tk.Tk()

# Crie um menu suspenso
menu = tk.Menu(window)

# Adicione três itens ao menu
menu.add_command(label="Imagem 1")
menu.add_command(label="Imagem 2")
menu.add_command(label="Imagem 3")

# Adicione o menu à barra de menus da janela
window.config(menu=menu)

# Crie uma área de texto
text_box = tk.Text(window)

# Posicione a área de texto no centro da janela
text_box.pack(center=True)

# Crie um botão para carregar a imagem
button = tk.Button(window, text="Carregar Imagem")

# Posicione o botão abaixo da área de texto
button.pack(below=text_box)

# Defina o evento de clique no botão
def load_image():
    # Obtenha a escolha do usuário no menu suspenso
    choice = menu.get()

    # Carregue a imagem correspondente
    if choice == "Imagem 1":
        image = tk.PhotoImage(file="image1.png")
    elif choice == "Imagem 2":
        image = tk.PhotoImage(file="image2.png")
    else:
        image = tk.PhotoImage(file="image3.png")

    # Exiba a imagem na área de texto
    text_box.image_create(tk.END, image=image)

# Vincule o evento de clique ao botão
button.config(command=load_image)

# Mostre a janela
window.mainloop()
