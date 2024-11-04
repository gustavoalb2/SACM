from datetime import datetime, timedelta
import tkinter as tk
import ttkbootstrap as ttk
from tkinter import messagebox
import sqlite3

def exibir_lista(app, dados, colunas, titulo):
    janela = ttk.Toplevel(app)
    janela.title(titulo)

    frame_pesquisa = tk.Frame(janela)
    frame_pesquisa.pack(fill=tk.X, pady=10)

    tk.Label(frame_pesquisa, text="Pesquisar:").pack(side=tk.LEFT, padx=5)
    entrada_pesquisa = tk.Entry(frame_pesquisa)
    entrada_pesquisa.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

    def pesquisar():
        termo = entrada_pesquisa.get().lower()
        dados_filtrados = [paciente for paciente in dados if paciente[1].lower().startswith(termo)]
        atualizar_treeview(dados_filtrados)

    tk.Button(frame_pesquisa, text="Pesquisar", command=pesquisar).pack(side=tk.LEFT, padx=5)

    tree = ttk.Treeview(janela, columns=colunas, show='headings')
    for col in colunas:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for item in dados:
        tree.insert('', tk.END, values=item)

    tree.pack(fill=tk.BOTH, expand=True)

    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(fill=tk.X, pady=10)

    if titulo == 'Listar Pacientes':
        btn_editar = ttk.Button(frame_botoes, style='warning', text="Editar", command=lambda: editar_paciente(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes, style='danger', text="Excluir", command=lambda: excluir_paciente(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes, style='success', text="Inserir",
                                 command=lambda: criar_formulario_paciente(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    if titulo == 'Listar Médicos':
        tree.column('horario_entrada', width=150)
        tree.column('horario_saida', width=150)
        btn_editar = ttk.Button(frame_botoes, style='warning', text="Editar", command=lambda: editar_medico(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes, style='danger', text="Excluir", command=lambda: excluir_medico(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes, style='success', text="Inserir",
                                 command=lambda: criar_formulario_medico(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    if titulo == 'Listar Consultas':
        btn_editar = ttk.Button(frame_botoes, style='warning', text="Editar", command=lambda: editar_consulta(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes, style='danger', text="Excluir", command=lambda: excluir_consulta(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes, style='success', text="Inserir",
                                 command=lambda: criar_formulario_consulta(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    if titulo == 'Listar Unidades de Saúde':
        btn_editar = ttk.Button(frame_botoes, style='warning', text="Editar", command=lambda: editar_unidade(tree))
        btn_editar.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_excluir = ttk.Button(frame_botoes, style='danger', text="Excluir", command=lambda: excluir_unidade(tree))
        btn_excluir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_inserir = ttk.Button(frame_botoes, style='success', text="Inserir",
                                 command=lambda: criar_formulario_unidade(app))
        btn_inserir.pack(side=tk.LEFT, padx=5, ipadx=20)

        btn_voltar = ttk.Button(frame_botoes, text="Voltar", command=lambda: fechar_janela(janela))
        btn_voltar.pack(side=tk.RIGHT, padx=5, ipadx=20)

    def atualizar_treeview(dados):
        for item in tree.get_children():
            tree.delete(item)
        for item in dados:
            tree.insert('', tk.END, values=item)

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

        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_paciente(
            entradas['nome'].get(),
            entradas['data de nascimento'].entry.get(),
            entradas['cpf'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['endereço'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', command=lambda: fechar_janela(janela), width=20)
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)

        janela.grid_columnconfigure(1, weight=1)

    def cadastrar_paciente(nome, data_nascimento, cpf, telefone, email, endereco, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Paciente (nome, data_nascimento, cpf, telefone, email, endereco)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, data_nascimento, cpf, telefone, email, endereco))
        conn.commit()
        conn.close()
        janela.destroy()
        messagebox.showinfo('Sucesso', 'Paciente cadastrado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Paciente')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)

    def editar_paciente(tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Selecione um paciente para editar')
            return

        item = tree.item(selecionado)
        paciente = item['values']
        cod_paciente = paciente[0]

        janela = tk.Toplevel()
        janela.title("Editar Paciente")
        janela.geometry("400x400")

        campos = ['Nome', 'Data de Nascimento', 'CPF', 'Telefone', 'Email', 'Endereço', 'Status']
        entradas = {}
        for i, campo in enumerate(campos):
            ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            if campo == 'Status':
                entrada = ttk.Combobox(janela, values=['Ativo', 'Inativo'])
            else:
                entrada = ttk.Entry(janela)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
            entradas[campo.lower()] = entrada

        entradas['nome'].insert(0, paciente[1])  
        entradas['data de nascimento'].insert(0, paciente[2])  
        entradas['cpf'].insert(0, paciente[3])  
        entradas['telefone'].insert(0, paciente[4])  
        entradas['email'].insert(0, paciente[5])  
        entradas['endereço'].insert(0, paciente[6])  
        entradas['status'].set(paciente[7])  

        ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_paciente(
            cod_paciente,
            entradas['nome'].get(),
            entradas['data de nascimento'].get(),
            entradas['cpf'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['endereço'].get(),
            entradas['status'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', command=lambda: fechar_janela(janela), width=20)
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)

        janela.grid_columnconfigure(1, weight=1)

    def confirm_edit_paciente(cod_paciente, nome, data_nascimento, cpf, telefone, email, endereco, status, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Paciente
            SET nome = ?, data_nascimento = ?, cpf = ?, telefone = ?, email = ?, endereco = ?, status = ?
            WHERE cod_paciente = ?
        ''', (nome, data_nascimento, cpf, telefone, email, endereco, status, cod_paciente))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Paciente atualizado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Paciente')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)
        janela.destroy()

    def excluir_paciente(tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um paciente para excluir')
            return
        item = tree.item(selected_item)
        paciente = item['values']
        cod_paciente = paciente[0]
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Paciente
            SET status = 'Desativado'
            WHERE cod_paciente = ?
        ''', (cod_paciente,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Paciente desativado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Paciente')
        dadospaciente = cursor.fetchall()
        conn.close()
        atualizar_treeview(dadospaciente)

    def criar_formulario_medico(app):
        janela = ttk.Toplevel(app)
        janela.title("Cadastrar Médico")
        janela.geometry("400x400")

        campos = ['Nome', 'Especialidade', 'Telefone', 'Email', 'horario_entrada',
                  'horario_saida']
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
            entradas['horario_entrada'].get(),
            entradas['horario_saida'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)
        janela.grid_columnconfigure(1, weight=1)

    def cadastrar_medico(nome, especialidade, telefone, email, horario_entrada, horario_saida,
                         janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Medico (nome, especialidade, telefone, email, horario_entrada, horario_saida)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, especialidade, telefone, email, horario_entrada, horario_saida))
        conn.commit()
        conn.close()
        janela.destroy()
        messagebox.showinfo('Sucesso', 'Médico cadastrado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medico')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)

    def editar_medico(tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Selecione um medico para editar')
            return

        item = tree.item(selecionado)
        medico = item['values']
        cod_medico = medico[0]  

        janela = tk.Toplevel()
        janela.title("Editar Medico")
        janela.geometry("400x400")

        campos = ['Nome', 'Especialidade', 'Telefone', 'Email', 'Horário de Entrada', 'Horário de Saída',
                  'Status']
        entradas = {}
        for i, campo in enumerate(campos):
            ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            if campo == 'Status':
                entrada = ttk.Combobox(janela, values=['Ativo', 'Inativo'])
            else:
                entrada = ttk.Entry(janela)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
            entradas[campo.lower()] = entrada

        entradas['nome'].insert(0, medico[1])  
        entradas['especialidade'].insert(0, medico[2])  
        entradas['telefone'].insert(0, medico[3])  
        entradas['email'].insert(0, medico[4]) 
        entradas['horario_entrada'].insert(0, medico[5])  
        entradas['horario_saida'].insert(0, medico[6])  
        entradas['status'].set(medico[7])  

        ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_medico(
            cod_medico,
            entradas['nome'].get(),
            entradas['especialidade'].get(),
            entradas['telefone'].get(),
            entradas['email'].get(),
            entradas['horario_entrada'].get(),
            entradas['horario_saida'].get(),
            entradas['status'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)
        janela.grid_columnconfigure(1, weight=1)

    def confirm_edit_medico(cod_medico, nome, especialidade, telefone, email, horario_entrada,
                            horario_saida, status, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Medico
            SET nome = ?, especialidade = ?, telefone = ?, email = ?, horario_entrada = ?, horario_saida = ?, status = ?
            WHERE cod_medico = ?
        ''', (nome, especialidade, telefone, email, horario_entrada, horario_saida, status, cod_medico))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Médico atualizado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medico')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)
        fechar_janela(janela)

    def excluir_medico(tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione um medico para excluir')
            return
        item = tree.item(selected_item)
        medico = item['values']
        cod_medico = medico[0]
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Medico
            SET status = 'Desativado'
            WHERE cod_medico = ?
        ''', (cod_medico,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Médico desativado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Medico')
        dadosmedico = cursor.fetchall()
        conn.close()
        atualizar_treeview(dadosmedico)

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

        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_unidade(
            entradas['nome'].get(),
            entradas['endereço'].get(),
            entradas['telefone'].get(),
            entradas['especialidades'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        janela.grid_columnconfigure(1, weight=1)
        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)

    def cadastrar_unidade(nome, endereco, telefone, especialidades, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Unidade_de_Saude (nome, endereco, telefone, especialidades)
            VALUES (?, ?, ?, ?)
        ''', (nome, endereco, telefone, especialidades))
        conn.commit()
        conn.close()
        janela.destroy()
        messagebox.showinfo('Sucesso', 'Unidade de saúde cadastrado com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Unidade_de_Saude')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)

    def editar_unidade(tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Selecione uma unidade para editar')
            return

        
        item = tree.item(selecionado)
        unidade = item['values']
        cod_unidade = unidade[0]  

        janela = tk.Toplevel()
        janela.title("Editar Unidade de Saúde")
        janela.geometry("400x400")

        campos = ['Nome', 'Endereço', 'Telefone', 'Especialidades', 'Status']
        entradas = {}
        for i, campo in enumerate(campos):
            ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            if campo == 'Status':
                entrada = ttk.Combobox(janela, values=['Ativo', 'Inativo'])
            else:
                entrada = ttk.Entry(janela)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
            entradas[campo.lower()] = entrada

        entradas['nome'].insert(0, unidade[1]) 
        entradas['endereço'].insert(0, unidade[2]) 
        entradas['telefone'].insert(0, unidade[3])  
        entradas['especialidades'].insert(0, unidade[4])  
        entradas['status'].set(unidade[5])  

        ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_unidade(
            cod_unidade,
            entradas['nome'].get(),
            entradas['endereço'].get(),
            entradas['telefone'].get(),
            entradas['especialidades'].get(),
            entradas['status'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)
        janela.grid_columnconfigure(1, weight=1)

    def confirm_edit_unidade(cod_unidade, nome, endereco, telefone, especialidades, status, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Unidade_de_Saude
            SET nome = ?, endereco = ?, telefone = ?, especialidades = ?, status = ?
            WHERE cod_unidade = ?
        ''', (nome, endereco, telefone, especialidades, status, cod_unidade))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Unidade atualizada com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Unidade_de_Saude')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)
        fechar_janela(janela)

    def excluir_unidade(tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione uma unidade para excluir')
            return
        item = tree.item(selected_item)
        unidade = item['values']
        cod_unidade = unidade[0]
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Unidade_de_Saude
            SET status = 'Desativado'
            WHERE cod_unidade = ?
        ''', (cod_unidade,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Unidade desativada com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Unidade_de_Saude')
        dadosunidade = cursor.fetchall()
        conn.close()
        atualizar_treeview(dadosunidade)

    def criar_formulario_consulta(app):
        janela = ttk.Toplevel(app)
        janela.title("Cadastrar Consulta")
        janela.geometry("400x400")

        campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade']
        entradas = {}

        for i, campo in enumerate(campos):
            ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)

            if campo == 'Data':
                entrada = ttk.DateEntry(janela, dateformat='%d-%m-%Y', firstweekday=6, bootstyle='danger')
            elif campo == 'Código do Paciente':
                entrada = ttk.Combobox(janela, values=obter_lista_pacientes())
            elif campo == 'Código do Médico':
                entrada = ttk.Combobox(janela, values=obter_lista_medicos())
            elif campo == 'Código da Unidade':
                entrada = ttk.Combobox(janela, values=obter_lista_unidades())
            else:
                entrada = ttk.Entry(janela)

            entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
            entradas[campo.lower()] = entrada

        ttk.Button(janela, text="Salvar", width=20, command=lambda: cadastrar_consulta(
            entradas['data'].entry.get(),
            entradas['horário'].get(),
            entradas['observações'].get(),
            entradas['código do paciente'].get().split(' - ')[0],
            entradas['código do médico'].get().split(' - ')[0],
            entradas['código da unidade'].get().split(' - ')[0],
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)

        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)

        janela.grid_columnconfigure(1, weight=1)

    def cadastrar_consulta(data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()

        data_datetime = datetime.strptime(data, "%d-%m-%Y")
        horario_datetime = datetime.strptime(horario, "%H:%M").time()

        consulta_datetime = datetime.combine(data_datetime, horario_datetime)
        tempo_minimo = timedelta(hours=1)  

        cursor.execute('SELECT horario_entrada, horario_saida FROM Medico WHERE cod_medico = ?', (cod_medico,))
        horario_medico = cursor.fetchone()
        horario_entrada = datetime.strptime(horario_medico[0], "%H:%M").time()
        horario_saida = datetime.strptime(horario_medico[1], "%H:%M").time()

        if not (horario_entrada <= horario_datetime < horario_saida):
            messagebox.showerror('Erro', 'A consulta deve estar dentro do horário de expediente do médico.')
            conn.close()
            return

        cursor.execute('''SELECT * FROM Consulta WHERE cod_paciente = ? AND data = ?''', (cod_paciente, data))
        consultas_paciente = cursor.fetchall()

        for consulta in consultas_paciente:
            horario_existente = datetime.strptime(consulta[2], "%H:%M").time()  
            consulta_existente_datetime = datetime.combine(data_datetime, horario_existente)

            if consulta_existente_datetime <= consulta_datetime < consulta_existente_datetime + tempo_minimo:
                messagebox.showerror('Erro',
                                     'Este paciente já tem uma consulta marcada para este horário.')
                conn.close()
                return

        cursor.execute('''SELECT * FROM Consulta WHERE cod_medico = ? AND data = ?''', (cod_medico, data))
        consultas_medico = cursor.fetchall()

        for consulta in consultas_medico:
            horario_existente = datetime.strptime(consulta[2], "%H:%M").time()  
            consulta_existente_datetime = datetime.combine(data_datetime, horario_existente)

            if consulta_existente_datetime <= consulta_datetime < consulta_existente_datetime + tempo_minimo:
                messagebox.showerror('Erro',
                                     'Este médico já tem uma consulta marcada para este horário.')
                conn.close()
                return

        if data == '' or horario == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
        else:
            cursor.execute('''INSERT INTO Consulta (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade)
                              VALUES (?, ?, ?, ?, ?, ?)''',
                           (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade))
            conn.commit()
            conn.close()
            janela.destroy()
            messagebox.showinfo('Sucesso', 'Consulta cadastrado com sucesso!')
            conn = sqlite3.connect('sistema_agendamento.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM Consulta')
            dadospaciente = cursor.fetchall()
            atualizar_treeview(dadospaciente)

    def editar_consulta(tree):
        selecionado = tree.selection()
        if not selecionado:
            messagebox.showerror('Erro', 'Selecione uma consulta para editar')
            return

        
        item = tree.item(selecionado)
        consulta = item['values']
        cod_consulta = consulta[0]  

        janela = tk.Toplevel()
        janela.title("Editar Consulta")
        janela.geometry("400x400")

        campos = ['Data', 'Horário', 'Observações', 'Código do Paciente', 'Código do Médico', 'Código da Unidade',
                  'Status']
        entradas = {}
        for i, campo in enumerate(campos):
            ttk.Label(janela, text=f'{campo}:').grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
            if campo == 'Status':
                entrada = ttk.Combobox(janela, values=['Confirmado', 'Cancelado', 'Realizado'])
            else:
                entrada = ttk.Entry(janela)
            entrada.grid(row=i, column=1, padx=10, pady=5, sticky=tk.EW)
            entradas[campo.lower()] = entrada
        
        entradas['data'].insert(0, consulta[1]) 
        entradas['horário'].insert(0, consulta[2])  
        entradas['observações'].insert(0, consulta[3])  
        entradas['código do paciente'].insert(0, consulta[4])  
        entradas['código do médico'].insert(0, consulta[5]) 
        entradas['código da unidade'].insert(0, consulta[6]) 
        entradas['status'].insert(0, consulta[7])  

        ttk.Button(janela, text="Salvar", width=20, command=lambda: confirm_edit_consulta(
            cod_consulta,
            entradas['data'].get(),
            entradas['horário'].get(),
            entradas['observações'].get(),
            entradas['código do paciente'].get(),
            entradas['código do médico'].get(),
            entradas['código da unidade'].get(),
            entradas['status'].get(),
            janela
        )).grid(row=len(campos), column=0, columnspan=2, pady=10)
        btn_voltar = ttk.Button(janela, text='Voltar', width=20, command=lambda: fechar_janela(janela))
        btn_voltar.grid(row=len(campos) + 1, column=0, columnspan=2)
        janela.grid_columnconfigure(1, weight=1)

    def confirm_edit_consulta(cod_consulta, data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, status,
                              janela):
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Consulta
            SET data = ?, horario = ?, observacoes = ?, cod_paciente = ?, cod_medico = ?, cod_unidade = ?, status = ?
            WHERE cod_consulta = ?
        ''', (data, horario, observacoes, cod_paciente, cod_medico, cod_unidade, status, cod_consulta))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Consulta atualizada com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Consulta')
        dadospaciente = cursor.fetchall()
        atualizar_treeview(dadospaciente)
        janela.destroy()

    def excluir_consulta(tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror('Erro', 'Selecione uma consulta para excluir')
            return
        item = tree.item(selected_item)
        consulta = item['values']
        cod_consulta = consulta[0]
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE Consulta
            SET status = 'Cancelado'
            WHERE cod_consulta = ?
        ''', (cod_consulta,))
        conn.commit()
        conn.close()
        messagebox.showinfo('Sucesso', 'Consulta cancelada com sucesso!')
        conn = sqlite3.connect('sistema_agendamento.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Consulta')
        dadosconsulta = cursor.fetchall()
        conn.close()
        atualizar_treeview(dadosconsulta)


def listar_pacientes(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Paciente')
    pacientes = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Data Nasc.', 'CPF', 'Telefone', 'Email', 'Endereço', 'Status']
    exibir_lista(app, pacientes, colunas, 'Listar Pacientes')


def listar_medicos(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Medico')
    medicos = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Especialidade', 'Telefone', 'Email', 'horario_entrada', 'horario_saida', 'Status']
    exibir_lista(app, medicos, colunas, 'Listar Médicos')


def listar_unidades(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Unidade_de_Saude')
    unidades = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Nome', 'Endereço', 'Telefone', 'Especialidades', 'Status']
    exibir_lista(app, unidades, colunas, 'Listar Unidades de Saúde')


def listar_consultas(app):
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Consulta')
    consultas = cursor.fetchall()
    conn.close()
    colunas = ['ID', 'Data', 'Horário', 'Observações', 'Paciente ID', 'Médico ID', 'Unidade ID', 'Status']
    exibir_lista(app, consultas, colunas, 'Listar Consultas')


def obter_lista_pacientes():
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cod_paciente, nome FROM Paciente")
    pacientes = cursor.fetchall()
    conn.close()
    return [f"{paciente[0]} - {paciente[1]}" for paciente in pacientes]


def obter_lista_medicos():
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cod_medico, nome FROM Medico")
    medicos = cursor.fetchall()
    conn.close()
    return [f"{medico[0]} - {medico[1]}" for medico in medicos]


def obter_lista_unidades():
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()
    cursor.execute("SELECT cod_unidade, nome FROM Unidade_de_Saude")
    unidades = cursor.fetchall()
    conn.close()
    return [f"{unidade[0]} - {unidade[1]}" for unidade in unidades]


def limpar_tela(app):
    for widget in app.winfo_children():
        widget.destroy()


def voltar(app):
    limpar_tela(app)


def fechar_janela(janela):
    janela.destroy()