import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('sistema_agendamento.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Paciente (
            cod_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_nascimento DATE,
            cpf TEXT,
            telefone TEXT,
            email TEXT,
            endereco TEXT,
            status TEXT DEFAULT 'Ativo'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Medico (
            cod_medico INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT,
            telefone TEXT,
            email TEXT,
            horario_entrada TEXT NOT NULL,
            horario_saida TEXT NOT NULL,
            status TEXT DEFAULT 'Ativo'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Unidade_de_Saude (
            cod_unidade INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            endereco TEXT,
            telefone TEXT,
            especialidades TEXT,
            status TEXT DEFAULT 'Ativo'
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Consulta (
            cod_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
            data DATE NOT NULL,
            horario DATE NOT NULL,
            observacoes TEXT,
            cod_paciente INTEGER,
            cod_medico INTEGER,
            cod_unidade INTEGER,
            status TEXT DEFAULT 'Agendada',
            FOREIGN KEY (cod_paciente) REFERENCES Paciente (cod_paciente),
            FOREIGN KEY (cod_medico) REFERENCES Medico (cod_medico),
            FOREIGN KEY (cod_unidade) REFERENCES Unidade_de_Saude (cod_unidade)
        )
    ''')

    conn.commit()
    conn.close()
