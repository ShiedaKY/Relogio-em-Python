import tkinter as tk
from tkinter import font
import time

def atualizar_horario():
    horario_atual = time.strftime("%H:%M:%S")
    lbl_horario.config(text=horario_atual)
    janela.after(1000, atualizar_horario)

def atualizar_data():
    data_atual = time.strftime("%d/%m/%Y")
    lbl_data.config(text=data_atual)
    janela.after(60000, atualizar_data)

def fechar_janela():
    janela.destroy()

# Cria uma janela
janela = tk.Tk()
janela.title("Relógio Digital")
janela.configure(bg="#222222")

# Define a fonte para o horário e a data
fonte_horario = font.Font(family="Helvetica", size=80, weight="bold")
fonte_data = font.Font(family="Helvetica", size=30, weight="bold")

# Cria uma label para exibir o horário
lbl_horario = tk.Label(janela, font=fonte_horario, fg="#ffffff", bg="#222222")
lbl_horario.pack(pady=50)

# Cria uma label para exibir a data
lbl_data = tk.Label(janela, font=fonte_data, fg="#ffffff", bg="#222222")
lbl_data.pack()

# Chama as funções para atualizar o horário e a data inicialmente
atualizar_horario()
atualizar_data()

# Cria um botão para fechar a janela
btn_fechar = tk.Button(janela, text="Fechar", font=("Helvetica", 16), command=fechar_janela, bg="#ff0000", fg="#ffffff")
btn_fechar.pack(pady=20)

# Define o tamanho e a posição da janela
largura_janela = 600
altura_janela = 300
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = int((largura_tela / 2) - (largura_janela / 2))
pos_y = int((altura_tela / 2) - (altura_janela / 2))
janela.geometry(f"{largura_janela}x{altura_janela}+{pos_x}+{pos_y}")

# Executa a janela
janela.mainloop()
