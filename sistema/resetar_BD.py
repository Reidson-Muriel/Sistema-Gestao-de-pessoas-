import os
from sistema.database.conexao import conectar, reset_BD, criar_tabela

modo = os.getenv("MODO") #ele pega o sistema em qual modo estara

if modo != "dev":
    print("Reset bloqueado, porque é usuario!!!")
    exit()

print("Lembre-se que isso vão apagar todos os dados")
confirmar = input("Digite CONFIRMAR para resetar-los: ")
if confirmar.upper() == "CONFIRMAR":
    conn = conectar()
    criar_tabela()
    reset_BD(conn)
    conn.close()
    print("Banco resetado com sucesso!")

else:
    print("Cancelado")