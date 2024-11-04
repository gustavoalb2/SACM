import os
import sys
import tkinter as tk
import ttkbootstrap as ttk
from db import criar_banco_de_dados
from forms import (listar_pacientes, listar_medicos, listar_consultas, listar_unidades)
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Obtenha o caminho absoluto para o recurso, funciona para dev e para PyInstaller """
    try:
        # PyInstaller cria uma pasta temporária e armazena o caminho nela
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def criar_interface():
    app = ttk.Window(themename='flatly')
    app.title("Sistema de Agendamento de Consultas Médicas")
    app.geometry("900x500")

    imagem_path = resource_path("src/SACM.png")
    imagem = Image.open(imagem_path)
    imagem = imagem.resize((900, 500), Image.LANCZOS)
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = tk.Label(app, image=imagem_tk)
    label_imagem.image = imagem_tk
    label_imagem.pack()

    menubar = ttk.Menu(app)
    app.config(menu=menubar)

    paciente_menu = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Pacientes", menu=paciente_menu)
    paciente_menu.add_command(label="Listar Pacientes", command=lambda: listar_pacientes(app))

    medico_menu = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Médicos", menu=medico_menu)
    medico_menu.add_command(label="Listar Médicos", command=lambda: listar_medicos(app))

    consulta_menu = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Consultas", menu=consulta_menu)
    consulta_menu.add_command(label="Listar Consultas", command=lambda: listar_consultas(app))

    unidade_menu = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Unidades de Saúde", menu=unidade_menu)
    unidade_menu.add_command(label="Listar Unidades de Saúde", command=lambda: listar_unidades(app))

    tema_menu = ttk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Temas", menu=tema_menu)

    for theme_name in app.style.theme_names():
        tema_menu.add_command(label=theme_name, command=lambda t=theme_name: app.style.theme_use(t))

    app.mainloop()

if __name__ == "__main__":
    criar_banco_de_dados()
    criar_interface()
