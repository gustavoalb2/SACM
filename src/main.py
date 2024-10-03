import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class Tela:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Tela')
        self.janela.geometry('900x800')

        self.mnu_barra = ttk.Menu(self.janela)
        self.mnu_paciente = ttk.Menu(self.mnu_barra, tearoff=0)
        self.mnu_medico = ttk.Menu(self.mnu_barra, tearoff=0, )
        self.mnu_agendamentos = ttk.Menu(self.mnu_barra, tearoff=0)
        
        self.mnu_barra.add_cascade(label='Pacientes', menu=self.mnu_paciente) 
        self.mnu_barra.add_cascade(label='Medicos', menu=self.mnu_medico) 
        self.mnu_barra.add_cascade(label='Agendamentos', menu=self.mnu_agendamentos) 
        self.mnu_paciente.add_command(label='Listar paciente', command=self.listar_pacientes)
        self.mnu_paciente.add_separator()
        self.mnu_paciente.add_command(label='Cadastrar paciente')
        
        self.mnu_medico.add_command(label='Listar medico')
        self.mnu_medico.add_separator()
        self.mnu_medico.add_command(label='Cadastrar medico')
        
        self.mnu_agendamentos.add_command(label='Listar agendamentos')
        self.mnu_agendamentos.add_separator()
        self.mnu_agendamentos.add_command(label='Cadastrar agendamentos')

        self.janela.config(menu=self.mnu_barra)

    def listar_pacientes(self):
        self.top_pacientes = ttk.Toplevel(self.janela)
        self.top_pacientes.title('Listar Pacientes')
        self.top_pacientes.geometry('900x800')

        colunas = ('ID', 'Nome', 'CPF', 'Telefone', 'Email', 'Endereco')
        self.tvw_pacientes = ttk.Treeview(self.top_pacientes, columns=colunas)
        self.tvw_pacientes.heading('#0', text='ID')
        self.tvw_pacientes.heading('#1', text='Nome')
        self.tvw_pacientes.heading('#2', text='CPF')
        self.tvw_pacientes.heading('#3', text='Telefone')
        self.tvw_pacientes.heading('#4', text='Email')
        self.tvw_pacientes.heading('#5', text='Endereco')
        self.tvw_pacientes.pack()

        self.tvw_pacientes.column('#0', width=50)

        self.tvw_pacientes.config()

janela = ttk.Window(themename='solar')
app = Tela(janela)
janela.mainloop()