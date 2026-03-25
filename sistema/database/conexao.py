import mysql.connector
import os
def conectar():
    print("conectando no local")
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="reidson_10",
        database="agenda"
    )

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100),
        nascimento DATE,
        telefone VARCHAR(20),
        email VARCHAR(100),
        endereco VARCHAR(255),
        observacao TEXT
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()

    print("Tabela verificada/criada com sucesso!")
    
