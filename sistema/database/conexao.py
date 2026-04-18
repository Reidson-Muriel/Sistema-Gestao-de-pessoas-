import os
import sqlite3
#o variavel pega o caminho completo na pasta onde este arquivo esta
base_dir = os.path.dirname(os.path.abspath(__file__))
# variavel monta o caminho completo no banco de dados
db_path = os.path.join(base_dir, "agenda.db")
def conectar():
    return sqlite3.connect(db_path)

def criar_tabela(conn):
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        telefone TEXT,
        email TEXT,
        endereco TEXT,
        observacao TEXT,
        data_nascimento TEXT
    )
    """)

    conn.commit()
    cursor.close()


def reset_BD(conn):
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contatos")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='contatos'")

    conn.commit()
    cursor.close()
    conn.close()
    
    
    
