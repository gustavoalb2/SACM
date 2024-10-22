from datetime import datetime
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3

#função para mostrar a lista de pacientes, médicos, consultas e unidades de saúde
def exibir_lista(app, dados, colunas, titulo):
    janela = ttk.Toplevel(app)
    janela.title(titulo)

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in dados:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)
    
    # Frame para os botões
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(fill=tk.X, pady=10)

    #botões para editar, excluir, inserir e voltar com base na tabela selecionada: paciente, médico, consulta ou unidade
    if titulo == 'Listar Pacientes':
        btn_editar = ttk.Button(frame_botoes, style='warning', text="Editar", command=lambda: editar_paciente(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes, style='danger', text="Excluir", command=lambda: excluir_paciente(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes, style='success', text="Inserir", command=lambda: criar_formulario_paciente(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)
    
        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)
        
    if titulo == 'Listar Médicos':
        btn_editar = ttk.Button(frame_botoes, style='warning',text="Editar", command=lambda: editar_medico(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes,style='danger', text="Excluir", command=lambda: excluir_medico(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes,style='success', text="Inserir", command=lambda: criar_formulario_medico(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    if titulo == 'Listar Consultas':
        btn_editar = ttk.Button(frame_botoes, style='warning',text="Editar", command=lambda: editar_consulta(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes,style='danger', text="Excluir", command=lambda: excluir_consulta(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes,style='success', text="Inserir", command=lambda: criar_formulario_consulta(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    if titulo == 'Listar Unidades de Saúde':
        btn_editar = ttk.Button(frame_botoes, style='warning',text="Editar", command=lambda: editar_unidade(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes,style='danger', text="Excluir", command=lambda: excluir_unidade(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes,style='success', text="Inserir", command=lambda: criar_formulario_unidade(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

#funções relacionadas a paciente abaixo
def cadastrar_paciente(nome, data_nascimento, cpf, telefone, email, endereco,janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Paciente (nome, data_nascimento, cpf, telefone, email, endereco)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, data_nascimento, cpf, telefone, email, endereco))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Paciente cadastrado com sucesso!')
def criar_formulario_paciente(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Paciente")
    janela.geometry("400x400")

    campos = ['Nome', 'Data de Nascimento', 'CPF', 'Telefone', 'Email', 'Endereço']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        if campo == 'Data de Nascimento':
            entrada = ttk.DateEntry(janela, dateformat='%d-%m-%Y',
                            firstweekday=6,
                            bootstyle='danger')
        else:
            entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    ttk.Button(janela, text="Salvar",width=20, command=lambda: cadastrar_paciente(
        entradas['nome'].get(),
        entradas['data de nascimento'].entry.get(),
        entradas['cpf'].get(),
        entradas['telefone'].get(),
        entradas['email'].get(),
        entradas['endereço'].get(),
        janela
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    btn_voltar = ttk.Button(janela, text='Voltar', command=lambda: fechar_janela(janela), width=20)
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)

    janela.grid_columnconfigure(1, weight=1)
def listar_pacientes(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Paciente')
    pacientes = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Data Nasc.', 'CPF', 'Telefone', 'Email', 'Endereço']
    exibir_lista(app, pacientes, colunas, 'Listar Pacientes')
def editar_paciente(tree):
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror('Erro', 'Selecione um paciente para editar')
        return
    
    # Obtém os dados do paciente selecionado
    item = tree.item(selecionado)
    paciente = item['values']
    cod_paciente = paciente[0]  # Supondo que o cod_paciente é o primeiro valor

    janela = tk.Toplevel()
    janela.title("Editar Paciente")
    janela.geometry("400x400")

    campos = ['Nome', 'Data de Nascimento', 'CPF', 'Telefone', 'Email', 'Endereço']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

    # Mapeia os valores do paciente para os campos correspondentes
    entradas['nome'].insert(0, paciente[1])  # Nome
    entradas['data de nascimento'].insert(0, paciente[2])  # Data de Nascimento
    entradas['cpf'].insert(0, paciente[3])  # CPF
    entradas['telefone'].insert(0, paciente[4])  # Telefone
    entradas['email'].insert(0, paciente[5])  # Email
    entradas['endereço'].insert(0, paciente[6])  # Endereço

    ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_paciente(
        cod_paciente,
        entradas['nome'].get(),
        entradas['data de nascimento'].get(),
        entradas['cpf'].get(),
        entradas['telefone'].get(),
        entradas['email'].get(),
        entradas['endereço'].get(),
        janela
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    btn_voltar = ttk.Button(janela, text='Voltar', command=lambda: fechar_janela(janela), width=20)
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)

    janela.grid_columnconfigure(1, weight=1)   
def confirm_edit_paciente(cod_paciente, nome, data_nascimento, cpf, telefone, email, endereco, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Paciente
        SET nome = ?, data_nascimento = ?, cpf = ?, telefone = ?, email = ?, endereco = ?
        WHERE cod_paciente = ?
    ''', (nome, data_nascimento, cpf, telefone, email, endereco, cod_paciente))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')
    fechar_janela(janela)  
def excluir_paciente(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um paciente para excluir')
        return
    if selected_item:
        item = tree.item(selected_item)
        paciente = item['values']
        # Lógica para excluir o paciente
        print(f"Excluir paciente: {paciente}")
    
#funções relacionadas a medico abaixo
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
def listar_medicos(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Medico')
    medicos = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Especialidade', 'Telefone', 'Email', 'Disponibilidade Dias', 'Disponibilidade Horário']
    exibir_lista(app, medicos, colunas, 'Listar Médicos')
def editar_medico(tree):
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror('Erro', 'Selecione um medico para editar')
        return
    
    # Obtém os dados do paciente selecionado
    item = tree.item(selecionado)
    medico = item['values']
    cod_medico = medico[0]  # Supondo que o cod_paciente é o primeiro valor

    janela = tk.Toplevel()
    janela.title("Editar Medico")
    janela.geometry("400x400")
    
    campos = ['Nome', 'Especialidade', 'Telefone', 'Email', 'Dias de Disponibilidade', 'Horário de Disponibilidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada
        
    # Mapeia os valores do paciente para os campos correspondentes
    entradas['nome'].insert(0, medico[1])  # Nome
    entradas['especialidade'].insert(0, medico[2])  # Data de Nascimento
    entradas['telefone'].insert(0, medico[3])  # CPF
    entradas['email'].insert(0, medico[4])  # Telefone
    entradas['dias de disponibilidade'].insert(0, medico[5])  # Email
    entradas['horário de disponibilidade'].insert(0, medico[6])  # Endereço

    ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_medico(
        cod_medico,
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
def confirm_edit_medico(cod_medico, nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Medico
        SET nome = ?, especialidade = ?, telefone = ?, email = ?, disponibilidade_dias = ?, disponibilidade_horario = ?
        WHERE cod_medico = ?
    ''', (nome, especialidade, telefone, email, disponibilidade_dias, disponibilidade_horario, cod_medico))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Médico atualizado com sucesso!')
    fechar_janela(janela)    
def excluir_medico(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione um medico para excluir')
        return
    if selected_item:
        item = tree.item(selected_item)
        medico = item['values']
        # Lógica para excluir o medico
        print(f"Excluir medico: {medico}") 

#funções relacionadas a consulta abaixo
def cadastrar_consulta(data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, janela):
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
def criar_formulario_consulta(app):
    janela = ttk.Toplevel(app)
    janela.title("Cadastrar Consulta")
    janela.geometry("400x400")

    campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        if campo == 'Data':
            entrada = ttk.DateEntry(janela, dateformat='%d-%m-%Y',
                            firstweekday=6,
                            bootstyle='danger')
        else:
            entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada

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
def listar_consultas(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Consulta')
    consultas = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Data', 'Horário', 'Observações', 'Paciente ID', 'Médico ID', 'Unidade ID']
    exibir_lista(app, consultas, colunas, 'Listar Consultas')
def editar_consulta(tree):
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror('Erro', 'Selecione uma consulta para editar')
        return
    
    # Obtém os dados da consulta selecionada
    item = tree.item(selecionado)
    consulta = item['values']
    cod_consulta = consulta[0]  # Supondo que o cod_consulta é o primeiro valor

    janela = tk.Toplevel()
    janela.title("Editar Consulta")
    janela.geometry("400x400")
    
    campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada
        
    # Mapeia os valores da consulta para os campos correspondentes
    entradas['data'].insert(0, consulta[1])  # Data
    entradas['horário'].insert(0, consulta[2])  # Horário
    entradas['observações'].insert(0, consulta[3])  # Observações
    entradas['código do paciente'].insert(0, consulta[4])  # Código do Paciente
    entradas['código do médico'].insert(0, consulta[5])  # Código do Médico
    entradas['código da unidade'].insert(0, consulta[6])  # Código da Unidade

    ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_consulta(
        cod_consulta,
        entradas['data'].get(),
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
def confirm_edit_consulta(cod_consulta, data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Consulta
        SET data = ?, horario = ?, observacoes = ?, cod_paciente = ?, cod_medico = ?, cod_unidade = ?
        WHERE cod_consulta = ?
    ''', (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, cod_consulta))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Consulta atualizada com sucesso!')
    fechar_janela(janela)
def excluir_consulta(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione uma consulta para excluir')
        return
    if selected_item:
        item = tree.item(selected_item)
        consulta = item['values']
        # Lógica para excluir a consulta
        print(f"Excluir consulta: {consulta}")

#funções relacionadas a unidade abaixo
def cadastrar_unidade(nome, endereco, telefone, especialidades, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Unidade_de_Saude (nome, endereco, telefone, especialidades)
        VALUES (?, ?, ?, ?)
    ''', (nome, endereco, telefone, especialidades))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Unidade cadastrada com sucesso!')
    fechar_janela(janela)
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

    ttk.Button(janela, text="Salvar",width=20, command=lambda: cadastrar_unidade(
        entradas['nome'].get(),
        entradas['endereço'].get(),
        entradas['telefone'].get(),
        entradas['especialidades'].get(),
        janela
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    janela.grid_columnconfigure(1, weight=1)
    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
def listar_unidades(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Unidade_de_Saude')
    unidades = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Endereço', 'Telefone', 'Especialidades']
    exibir_lista(app, unidades, colunas, 'Listar Unidades de Saúde')
def editar_unidade(tree):
    selecionado = tree.selection()
    if not selecionado:
        messagebox.showerror('Erro', 'Selecione uma unidade para editar')
        return
    
    # Obtém os dados da unidade selecionada
    item = tree.item(selecionado)
    unidade = item['values']
    cod_unidade = unidade[0]  # Supondo que o cod_unidade é o primeiro valor

    janela = tk.Toplevel()
    janela.title("Editar Unidade de Saúde")
    janela.geometry("400x400")
    
    campos = ['Nome', 'Endereço', 'Telefone', 'Especialidades']
    entradas = {}
    for i, campo in enumerate(campos):
        ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entrada = ttk.Entry(janela)
        entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
        entradas[campo.lower()] = entrada
        
    # Mapeia os valores da unidade para os campos correspondentes
    entradas['nome'].insert(0, unidade[1])  # Nome
    entradas['endereço'].insert(0, unidade[2])  # Endereço
    entradas['telefone'].insert(0, unidade[3])  # Telefone
    entradas['especialidades'].insert(0, unidade[4])  # Especialidades

    ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_unidade(
        cod_unidade,
        entradas['nome'].get(),
        entradas['endereço'].get(),
        entradas['telefone'].get(),
        entradas['especialidades'].get(),
        janela
    )).grid(row=len(campos), column=0, columnspan=2, pady=10)
    btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
    btn_voltar.grid(row=len(campos)+1, column=0, columnspan=2)
    janela.grid_columnconfigure(1, weight=1)
def confirm_edit_unidade(cod_unidade, nome, endereco, telefone, especialidades, janela):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE Unidade_de_Saude
        SET nome = ?, endereco = ?, telefone = ?, especialidades = ?
        WHERE cod_unidade = ?
    ''', (nome, endereco, telefone, especialidades, cod_unidade))
    conn.commit()
    conn.close()
    messagebox.showinfo('Sucesso', 'Unidade atualizada com sucesso!')
    fechar_janela(janela)
def excluir_unidade(tree):
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Erro', 'Selecione uma unidade para excluir')
        return
    if selected_item:
        item = tree.item(selected_item)
        unidade = item['values']
        # Lógica para excluir a unidade
        print(f"Excluir unidade: {unidade}")

def limpar_tela(app):
    for widget in app.winfo_children():
        widget.destroy()

def voltar(app):
    limpar_tela(app)
    
def fechar_janela(janela):
    janela.destroy()