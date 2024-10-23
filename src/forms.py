from datetime import datetime
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3

def cadastrar_paciente(nome, data_nascimento, cpf, telefone, email, endereco, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Paciente (nome, data_nascimento, cpf, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, data_nascimento, cpf, telefone, email, endereco))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Paciente cadastrado com sucesso!')
    fechar_janela(janela)
    listar_pacientes(app)

def editar_paciente(id_paciente, nome, data_nascimento, cpf, telefone, email, endereco, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Paciente
        SET nome = ?, data_nascimento = ?, cpf = ?, telefone = ?, email = ?, endereco = ?
        WHERE cod_paciente = ?
    ''', (nome, data_nascimento, cpf, telefone, email, endereco, id_paciente))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')
    fechar_janela(janela)
    listar_pacientes(app)

def excluir_paciente(id_paciente,janela, app):
    if messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir este paciente?'):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Paciente WHERE cod_paciente = ?', (id_paciente,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Paciente excluído com sucesso!')

        fechar_janela(janela)

        listar_pacientes(app)


def criar_formulario_paciente(app, paciente=None):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Paciente")
    janela.geometry("400x400")

    campos = ['Nome', 'Data de Nascimento', 'CPF', 'Telefone', 'Email', 'Endereço']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        if campo == 'Data de Nascimento':
            entrada = ttk.DateEntry(janela, dateformat='%Y-%m-%d', bootstyle='danger')
            entrada.entry.delete(0, tk.END)
            entrada.entry.insert(0, paciente[i+1] if paciente else '')
        else:
            entrada = ttk.Entry(janela)
            entrada.insert(0, paciente[i + 1] if paciente else '')
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada


    if paciente:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: editar_paciente(
            paciente[0],
            entradas['nome'].get(),
            entradas['data de nascimento'].entry.get(),
            entradas['cpf'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['endereço'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    else:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_paciente(
            entradas['nome'].get(),
            entradas['data de nascimento'].entry.get(),
            entradas['cpf'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['endereço'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
    janela.grid_columnconfigure(1, weight=1)

def criar_formulario_medico(app, medico=None):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Médico")
    janela.geometry("400x400")

    campos = ['Nome', 'Especialidade', 'Telefone', 'Email', 'Dias de Disponibilidade', 'Horário de Disponibilidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.insert(0, medico[i + 1] if medico else '')
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    if medico:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: editar_medico(
            medico[0],
            entradas['nome'].get(),
            entradas['especialidade'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['dias de disponibilidade'].get(),
            entradas['horário de disponibilidade'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    else:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_medico(
            entradas['nome'].get(),
            entradas['especialidade'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['dias de disponibilidade'].get(),
            entradas['horário de disponibilidade'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
    janela.grid_columnconfigure(1, weight=1)

def cadastrar_medico(nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Medico (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Médico cadastrado com sucesso!')
    fechar_janela(janela)

def excluir_medico(id_medico, janela, app):
    if messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir este médico?'):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Medico WHERE cod_medico = ?', (id_medico,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Médico excluído com sucesso!')
        fechar_janela(janela)
        listar_medicos(app)

def editar_medico(id_medico, nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Medico
        SET nome = ?, especialidade = ?, telefone = ?, email = ?, disponibilidade_dias = ?, disponibilidade_horario = ?
        WHERE cod_medico = ?
    ''', (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario, id_medico))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Médico atualizado com sucesso!')
    fechar_janela(janela)
    listar_medicos(app)

def listar_medicos(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Medico')
    medicos = cursor.fetchall()
    conn.close()

    colunas = ['ID', 'Nome', 'Especialidade', 'Telefone', 'Email', 'Disponibilidade Dias', 'Disponibilidade Horário']
    janela = ttk.Toplevel(app)
    janela.title("Listar Médicos")
    janela.geometry("600x400")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in medicos:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

    def selecionar_item(event):
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            criar_formulario_medico(app, medico=item)

    def excluir_item():
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            excluir_medico(item[0], janela, app)
            tree.delete(item_selecionado)
            janela.destroy()

    ttk.Button(janela, text="Incluir", command=lambda: criar_formulario_medico(app), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Editar", command=lambda: selecionar_item(None), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Excluir", command=excluir_item, width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Voltar", command=lambda: fechar_janela(janela), width=20).pack(side=tk.RIGHT, padx=10, pady=10)



def cadastrar_consulta(data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    if data == '' or horario == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
    else:
        cursor.execute('''
            INSERT INTO Consulta (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Consulta cadastrada com sucesso!')
        fechar_janela(janela)
        listar_consultas(app)

def criar_formulario_consulta(app, consulta=None):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Consulta")
    janela.geometry("400x400")

    campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        if campo == 'Data':
            entrada = ttk.DateEntry(janela, dateformat='%Y-%m-%d', bootstyle='danger')
            entrada.entry.delete(0, tk.END)
            entrada.entry.insert(0, consulta[i+1] if consulta else '')
        else:
            entrada = ttk.Entry(janela)
            entrada.insert(0, consulta[i+1] if consulta else '')
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    if consulta:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: editar_consulta(
            consulta[0],
            entradas['data'].entry.get(),
            entradas['horário'].get(),
            entradas['observações'].get(),
            entradas['código do paciente'].get(),
            entradas['código do médico'].get(),
            entradas['código da unidade'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    else:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_consulta(
            entradas['data'].entry.get(),
            entradas['horário'].get(),
            entradas['observações'].get(),
            entradas['código do paciente'].get(),
            entradas['código do médico'].get(),
            entradas['código da unidade'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
    janela.grid_columnconfigure(1, weight=1)

def editar_consulta(id_consulta, data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Consulta
        SET data = ?, horario = ?, observacoes = ?, cod_paciente = ?, cod_medico = ?, cod_unidade = ?
        WHERE cod_consulta = ?
    ''', (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, id_consulta))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Consulta atualizada com sucesso!')
    fechar_janela(janela)
    listar_consultas(app)

def excluir_consulta(id_consulta, janela, app):
    if messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir esta consulta?'):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Consulta WHERE cod_consulta = ?', (id_consulta,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Consulta excluída com sucesso!')
        fechar_janela(janela)
        listar_consultas(app)


def cadastrar_unidade(nome, endereco, telefone, especialidades, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Unidade_de_Saude (nome, endereco, telefone, especialidades)
        VALUES (?, ?, ?, ?)
    ''', (nome, endereco, telefone, especialidades))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Unidade de Saúde cadastrada com sucesso!')
    fechar_janela(janela)
    listar_unidades(app)

def criar_formulario_unidade(app, unidade=None):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Unidade de Saúde")
    janela.geometry("400x400")

    campos = ['Nome', 'Endereço', 'Telefone', 'Especialidades']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.insert(0, unidade[i + 1] if unidade else '')
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    if unidade:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: editar_unidade(
            unidade[0],
            entradas['nome'].get(),
            entradas['endereço'].get(),
            entradas['telefone'].get(),
            entradas['especialidades'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    else:
        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_unidade(
            entradas['nome'].get(),
            entradas['endereço'].get(),
            entradas['telefone'].get(),
            entradas['especialidades'].get(),
            janela,
            app
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)

    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
    janela.grid_columnconfigure(1, weight=1)

def editar_unidade(id_unidade, nome, endereco, telefone, especialidades, janela, app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Unidade_de_Saude
        SET nome = ?, endereco = ?, telefone = ?, especialidades = ?
        WHERE cod_unidade = ?
    ''', (nome, endereco, telefone, especialidades, id_unidade))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Unidade de Saúde atualizada com sucesso!')
    fechar_janela(janela)
    listar_unidades(app)

def excluir_unidade(id_unidade, janela, app):
    if messagebox.askyesno('Confirmar Exclusão', 'Tem certeza que deseja excluir esta unidade de saúde?'):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM Unidade_de_Saude WHERE cod_unidade = ?', (id_unidade,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Unidade de Saúde excluída com sucesso!')
        fechar_janela(janela)
        listar_unidades(app)



def exibir_lista(app, dados, colunas, titulo, entidade):
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

    def selecionar_item(event):
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            if entidade == 'paciente':
                criar_formulario_paciente(app, paciente=item)

    def excluir_item():
        try:
            if tree.winfo_exists():
                item_selecionado = tree.selection()
                if item_selecionado:
                    item = tree.item(item_selecionado)['values']
                    if entidade == 'paciente':
                        excluir_paciente(item[0], janela, app)
                        tree.delete(item_selecionado)
                        janela.destroy()
            else:
                print("O Treeview já foi destruído.")
        except Exception as e:
            print(f"Erro ao excluir o item: {e}")

    ttk.Button(janela, text="Incluir", command=lambda: criar_formulario_paciente(app), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Editar", command=lambda: selecionar_item(None), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Excluir", command=excluir_item, width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Voltar", command=lambda: fechar_janela(janela), width=20).pack(side=tk.RIGHT, padx=10, pady=10)

def listar_pacientes(app):

    for widget in app.winfo_children():
        if isinstance(widget, ttk.Toplevel):
            widget.destroy()

    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Paciente')
    pacientes = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Data Nasc.', 'CPF', 'Telefone', 'Email', 'Endereço']
    exibir_lista(app, pacientes, colunas, 'Listar Pacientes', 'paciente')

def listar_medicos(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Medico')
    medicos = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Especialidade', 'Telefone', 'Email', 'Disponibilidade Dias', 'Disponibilidade Horário']
    exibir_lista(app, medicos, colunas, 'Listar Médicos','medico')

def listar_consultas(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Consulta')
    consultas = cursor.fetchall()
    conn.close()

    colunas = ['ID', 'Data', 'Horário', 'Observações', 'Paciente', 'Médico', 'Unidade']
    janela = ttk.Toplevel(app)
    janela.title("Listar Consultas")
    janela.geometry("600x400")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in consultas:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

    def selecionar_item(event):
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            criar_formulario_consulta(app, consulta=item)

    def excluir_item():
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            excluir_consulta(item[0], janela, app)
            tree.delete(item_selecionado)
            janela.destroy()

    ttk.Button(janela, text="Incluir", command=lambda: criar_formulario_consulta(app), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Editar", command=lambda: selecionar_item(None), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Excluir", command=excluir_item, width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Voltar", command=lambda: fechar_janela(janela), width=20).pack(side=tk.RIGHT, padx=10, pady=10)


def listar_unidades(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Unidade_de_Saude')
    unidades = cursor.fetchall()
    conn.close()

    colunas = ['ID', 'Nome', 'Endereço', 'Telefone', 'Especialidades']
    janela = ttk.Toplevel(app)
    janela.title("Listar Unidades de Saúde")
    janela.geometry("600x400")

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in unidades:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

    def selecionar_item(event):
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            fechar_janela(janela)
            criar_formulario_unidade(app, unidade=item)

    def excluir_item():
        item_selecionado = tree.selection()
        if item_selecionado:
            item = tree.item(item_selecionado)['values']
            excluir_unidade(item[0], janela, app)
            tree.delete(item_selecionado)
            fechar_janela(janela)

    ttk.Button(janela, text="Incluir", command=lambda: criar_formulario_unidade(app), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Editar", command=lambda: selecionar_item(None), width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Excluir", command=excluir_item, width=20).pack(side=tk.LEFT, padx=10, pady=10)
    ttk.Button(janela, text="Voltar", command=lambda: fechar_janela(janela), width=20).pack(side=tk.RIGHT, padx=10, pady=10)


def limpar_tela(app):
    for widget in app.winfo_children():
        widget.destroy()

def voltar(app):
    limpar_tela(app)
    app.__init__(app)

def fechar_janela(janela):
    janela.destroy()