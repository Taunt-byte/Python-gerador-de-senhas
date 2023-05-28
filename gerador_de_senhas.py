import random
import string
import tkinter as tk

def gerar_senha(tamanho=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_nova_senha():
    tamanho_senha = int(entry_tamanho.get())
    senha_gerada = gerar_senha(tamanho_senha)
    lbl_senha.config(text="Senha gerada: " + senha_gerada)

# Cria a janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Cria os elementos da tela
lbl_tamanho = tk.Label(janela, text="Tamanho da senha:")
lbl_tamanho.pack()

entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

btn_gerar_senha = tk.Button(janela, text="Gerar Senha", command=gerar_nova_senha)
btn_gerar_senha.pack()

lbl_senha = tk.Label(janela, text="Senha gerada:")
lbl_senha.pack()

# Inicia o loop da janela
janela.mainloop()
