import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from db import criar_banco_de_dados
from forms import (criar_formulario_paciente, criar_formulario_medico,
                   criar_formulario_consulta, criar_formulario_unidade,
                   listar_pacientes, listar_medicos, listar_consultas, listar_unidades)

def criar_interface():
    app = tb.Window(themename='flatly')
    app.title("Sistema de Agendamento de Consultas")
    app.geometry("600x400")

    menubar = tb.Menu(app)
    app.config(menu=menubar)

    paciente_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Pacientes", menu=paciente_menu)
    paciente_menu.add_command(label="Cadastrar Paciente", command=lambda: criar_formulario_paciente(app))
    paciente_menu.add_command(label="Listar Pacientes", command=lambda: listar_pacientes(app))

    medico_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Médicos", menu=medico_menu)
    medico_menu.add_command(label="Cadastrar Médico", command=lambda: criar_formulario_medico(app))
    medico_menu.add_command(label="Listar Médicos", command=lambda: listar_medicos(app))

    consulta_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Consultas", menu=consulta_menu)
    consulta_menu.add_command(label="Cadastrar Consulta", command=lambda: criar_formulario_consulta(app))
    consulta_menu.add_command(label="Listar Consultas", command=lambda: listar_consultas(app))

    unidade_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Unidades de Saúde", menu=unidade_menu)
    unidade_menu.add_command(label="Cadastrar Unidade", command=lambda: criar_formulario_unidade(app))
    unidade_menu.add_command(label="Listar Unidades de Saúde", command=lambda: listar_unidades(app))

    tema_menu = tb.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Temas", menu=tema_menu)

    for theme_name in app.style.theme_names():
        tema_menu.add_command(label=theme_name, command=lambda t=theme_name: app.style.theme_use(t))

    app.mainloop()

if __name__ == "__main__":
    criar_banco_de_dados()
    criar_interface()