import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap import Style
# import sqlite3

# Conectando ao banco de dados
# conn = sqlite3.connect('database\consultas.db')
# cursor = conn.cursor()

# Criando a tabela de pacientes
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS pacientes (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     data_nascimento TEXT,
#     cpf TEXT,
#     telefone TEXT,
#     email TEXT,
#     endereco TEXT
# )
# ''')

# Inserindo um paciente
# cursor.execute('''
# INSERT INTO pacientes (nome, data_nascimento, cpf, telefone, email, endereco)
# VALUES (?, ?, ?, ?, ?, ?)
# ''', ("Maria Oliveira", "1985-03-10", "98765432100", "999887766", "maria@example.com", "Rua B, 456"))

# Salvando as mudanças
# conn.commit()

# Consultando todos os pacientes
# cursor.execute('SELECT * FROM pacientes')
# pacientes = cursor.fetchall()

# Exibindo os pacientes
# for paciente in pacientes:
#     print(paciente)

# Atualizando o telefone de um paciente
# cursor.execute('''
# UPDATE pacientes
# SET telefone = ?
# WHERE cpf = ?
# ''', ("999665544", "98765432100"))

# Salvando as mudanças
# conn.commit()

# Fechando a conexão
# conn.close()


class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Tela')
        self.janela.geometry('900x800')

        self.mnu_barra = ttk.Menu(self.janela)
        self.mnu_paciente = ttk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_medico = ttk.Menu(self.mnu_barra, tearoff=0, )
        self.mnu_agendamentos = ttk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_config = ttk.Menu(self.mnu_barra, tearoff=0)
        
        self.mnu_barra.add_cascade(label='Pacientes', menu=self.mnu_paciente) 
        self.mnu_barra.add_cascade(label='Medicos', menu=self.mnu_medico) 
        self.mnu_barra.add_cascade(label='Agendamentos', menu=self.mnu_agendamentos) 
        self.mnu_barra.add_cascade(label='Configurações', menu=self.mnu_config)
        
        self.mnu_paciente.add_command(label='Listar paciente', command=self.listar_pacientes)
        self.mnu_paciente.add_separator()
        self.mnu_paciente.add_command(label='Cadastrar paciente', command=self.cadastrar_paciente)
        
        self.mnu_medico.add_command(label='Listar medico')
        self.mnu_medico.add_separator()
        self.mnu_medico.add_command(label='Cadastrar medico')
        
        self.mnu_agendamentos.add_command(label='Listar agendamentos')
        self.mnu_agendamentos.add_separator()
        self.mnu_agendamentos.add_command(label='Cadastrar agendamentos')
        
        self.mnu_config.add_command(label='Temas', command=self.mudar_tema)

        self.janela.config(menu=self.mnu_barra)

    def listar_pacientes(self):
        self.limpar_tela()
        self.janela.title('Listar Pacientes')
        self.janela.geometry('900x800')

        self.frm = ttk.Frame(self.janela)
        self.frm.pack()
        
        colunas = ['ID', 'Nome', 'CPF', 'Telefone', 'Email', 'Endereco']
        self.tvw_pacientes = ttk.Treeview(self.frm, columns=colunas, show='headings', height=20)
        self.tvw_pacientes.heading('ID', text='ID')
        self.tvw_pacientes.heading('Nome', text='Nome')
        self.tvw_pacientes.heading('CPF', text='CPF')
        self.tvw_pacientes.heading('Telefone', text='Telefone')
        self.tvw_pacientes.heading('Email', text='Email')
        self.tvw_pacientes.heading('Endereco', text='Endereco')
        self.tvw_pacientes.grid(row=0, column=0, padx=10, pady=10)

        self.tvw_pacientes.column('ID', width=50)
        self.tvw_pacientes.column('Nome', width=200)
        self.tvw_pacientes.column('CPF', width=100)
        self.tvw_pacientes.column('Telefone', width=100)
        self.tvw_pacientes.column('Email', width=150)
        self.tvw_pacientes.column('Endereco', width=150)
        
        self.tvw_pacientes.insert('', 'end', values=(1, 'Gustavo Oliveira Albuquerque', '123.456.789-00', '(11) 99999-9999', 'joseabluble@gmail.com', 'Rua das Flores, 123'))
        self.tvw_pacientes.config()
        
        self.btn_voltar = ttk.Button(self.frm, text='Voltar', command=self.voltar, style='info')
        self.btn_voltar.grid(row=1, column=0, ipadx=80)
    
    def cadastrar_paciente(self):
        self.limpar_tela()
        self.janela.title('Cadastrar Paciente')
        self.janela.geometry('900x800')
        
        self.frm = ttk.Frame(self.janela)
        self.frm.pack()
        
        self.label_nome = ttk.Label(self.frm, text='Nome:')
        self.label_nome.grid(row=0, column=0, padx=10, pady=10)
        self.entry_nome = ttk.Entry(self.frm, width=50)
        self.entry_nome.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_cpf = ttk.Label(self.frm, text='CPF:')
        self.label_cpf.grid(row=1, column=0, padx=10, pady=10)
        self.entry_cpf = ttk.Entry(self.frm)
        self.entry_cpf.grid(row=1, column=1, sticky='w', padx=10, pady=10)
        
        self.label_telefone = ttk.Label(self.frm, text='Telefone:')
        self.label_telefone.grid(row=2, column=0, padx=10, pady=10)
        self.entry_telefone = ttk.Entry(self.frm)
        self.entry_telefone.grid(row=2, column=1, sticky='w', padx=10, pady=10)
        
        self.label_email = ttk.Label(self.frm, text='Email:')
        self.label_email.grid(row=3, column=0, padx=10, pady=10)
        self.entry_email = ttk.Entry(self.frm, width=50)
        self.entry_email.grid(row=3, column=1, padx=10, pady=10)
        
        self.label_endereco = ttk.Label(self.frm, text='Endereco:')
        self.label_endereco.grid(row=4, column=0, padx=10, pady=10)
        self.txt_endereco = ttk.Text(self.frm, wrap=ttk.WORD, height=2, width=50)
        self.txt_endereco.grid(row=4, column=1)
        
        self.btn_salvar = ttk.Button(self.frm, text='Salvar', style='success')
        self.btn_salvar.grid(row=5, column=0, columnspan=2, padx=10, pady=10, ipadx=80)
        
        self.bnt_voltar = ttk.Button(self.frm, text='Voltar', command=self.voltar, style='info')
        self.bnt_voltar.grid(row=6, column=0, columnspan=2, padx=10, ipadx=80)
        
    def mudar_tema(self):
        self.top_tema = ttk.Toplevel(self.janela)
        self.top_tema.title('Temas')
        self.top_tema.geometry('900x200')
        self.style = Style() 
        
        #frame com todos os temas
        self.frm_tema = ttk.LabelFrame(self.top_tema, text="Temas do TTk BootStrap")
        self.frm_tema.pack()
        
        self.tema_selecionado = ttk.StringVar(value=self.style.theme_use())
        
        #radio button para escolher o tema, todos os temas
        colunas_por_linha = 8
        linha = 0
        coluna = 0
        for tema in self.style.theme_names():
            rb = ttk.Radiobutton(self.frm_tema, text=tema, value=tema, variable=self.tema_selecionado, command=self.change_tema)
            rb.grid(row=linha, column=coluna, padx=3)
            coluna += 1
            if coluna > colunas_por_linha:
                coluna = 0
                linha += 1   
        
        self.btnvoltar = ttk.Button(self.top_tema, text='Voltar', command=self.voltar, style='info')
        self.btnvoltar.pack()
    
    def change_tema(self):
        tema_selecionado = self.tema_selecionado.get()
        self.style.theme_use(tema_selecionado)

    def limpar_tela(self):
        for widget in self.janela.winfo_children():
            widget.destroy()

    def voltar(self):
            self.limpar_tela()
            self.__init__(self.janela)
    
janela = ttk.Window(themename='solar')
app = Tela(janela)
janela.mainloop()