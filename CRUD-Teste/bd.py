import sqlite3

def criar_banco_de_dados():
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Droga (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Arma (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            tipo TEXT NOT NULL,
            calibre TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def inserir_droga(nome, quantidade, preco):
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Droga (nome, quantidade, preco) VALUES (?, ?, ?)', (nome, quantidade, preco))
    conn.commit()
    conn.close()

def inserir_arma(nome, tipo, calibre):
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Arma (nome, tipo, calibre) VALUES (?, ?, ?)', (nome, tipo, calibre))
    conn.commit()
    conn.close()

def listar_drogas():
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Droga')
    drogas = cursor.fetchall()
    conn.close()
    return drogas

def listar_armas():
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Arma')
    armas = cursor.fetchall()
    conn.close()
    return armas

def excluir_armas(sql):
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print('ai')
    conn.close()

def atualizar_arma(sql):
    conn = sqlite3.connect('../../TESI1/Estudo Prova TESI/boca_de_fumo.db')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print('ai')
    conn.close()
