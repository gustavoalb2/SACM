import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3

def cadastrar_paciente(nome, data_nascimento, cpf, telefone, email, endereco):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Paciente (nome, data_nascimento, cpf, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, data_nascimento, cpf, telefone, email, endereco))
    conn.commit()
    conn.close()

def criar_formulario_paciente(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Paciente")
    janela.geometry("400x400")

    campos = ['Nome', 'Data de Nascimento', 'CPF', 'Telefone', 'Email', 'Endereço']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    ttk.Button(janela, text="Salvar", command=lambda: cadastrar_paciente(
        entradas['nome'].get(),
        entradas['data de nascimento'].get(),
        entradas['cpf'].get(),
        entradas['telefone'].get(),
        entradas['email'].get(),
        entradas['endereço'].get()
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    janela.grid_columnconfigure(1, weight=1)

def cadastrar_medico(nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Medico (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario))
    conn.commit()
    conn.close()

def criar_formulario_medico(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Médico")
    janela.geometry("400x400")

    campos = ['Nome', 'Especialidade', 'Telefone', 'Email', 'Dias de Disponibilidade', 'Horário de Disponibilidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    ttk.Button(janela, text="Salvar", command=lambda: cadastrar_medico(
        entradas['nome'].get(),
        entradas['especialidade'].get(),
        entradas['telefone'].get(),
        entradas['email'].get(),
        entradas['dias de disponibilidade'].get(),
        entradas['horário de disponibilidade'].get()
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    janela.grid_columnconfigure(1, weight=1)

def cadastrar_consulta(data, horario, observacoes, cod_paciente, cod_medico, cod_unidade):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Consulta (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade))
    conn.commit()
    conn.close()

def criar_formulario_consulta(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Consulta")
    janela.geometry("400x400")

    campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    ttk.Button(janela, text="Salvar", command=lambda: cadastrar_consulta(
        entradas['data'].get(),
        entradas['horário'].get(),
        entradas['observações'].get(),
        entradas['código do paciente'].get(),
        entradas['código do médico'].get(),
        entradas['código da unidade'].get()
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    janela.grid_columnconfigure(1, weight=1)

def cadastrar_unidade(nome, endereco, telefone, especialidades):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Unidade_de_Saude (nome, endereco, telefone, especialidades)
        VALUES (?, ?, ?, ?)
    ''', (nome, endereco, telefone, especialidades))
    conn.commit()
    conn.close()

def criar_formulario_unidade(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Unidade de Saúde")
    janela.geometry("400x400")

    campos = ['Nome', 'Endereço', 'Telefone', 'Especialidades']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    ttk.Button(janela, text="Salvar", command=lambda: cadastrar_unidade(
        entradas['nome'].get(),
        entradas['endereço'].get(),
        entradas['telefone'].get(),
        entradas['especialidades'].get()
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    janela.grid_columnconfigure(1, weight=1)


def exibir_lista(app, dados, colunas, titulo):
    janela = ttk.Toplevel(app)
    janela.title(titulo)
    janela.geometry("600x400")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in dados:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

def listar_pacientes(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Paciente')
    pacientes = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Data Nasc.', 'CPF', 'Telefone', 'Email', 'Endereço']
    exibir_lista(app, pacientes, colunas, 'Listar Pacientes')

def listar_medicos(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Medico')
    medicos = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Especialidade', 'Telefone', 'Email', 'Disponibilidade Dias', 'Disponibilidade Horário']
    exibir_lista(app, medicos, colunas, 'Listar Médicos')

def listar_consultas(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Consulta')
    consultas = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Data', 'Horário', 'Observações', 'Paciente ID', 'Médico ID', 'Unidade ID']
    exibir_lista(app, consultas, colunas, 'Listar Consultas')

def listar_unidades(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Unidade_de_Saude')
    unidades = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Endereço', 'Telefone', 'Especialidades']
    exibir_lista(app, unidades, colunas, 'Listar Unidades de Saúde')