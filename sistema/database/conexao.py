import sqlite3
def conectar():
    print("conectando no sqlite")
    return sqlite3.connect("agenda.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        data_nascimento TEXT,
        telefone TEXT,
        email TEXT,
        endereco TEXT,
        observacao TEXT
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela verificada/criada com sucesso!")
    
