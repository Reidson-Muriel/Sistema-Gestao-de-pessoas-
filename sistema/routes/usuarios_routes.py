from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, request, session
from sistema.utils.response import resp_sucess, resp_erro
from sistema.database.conexao import conectar
from sistema.routes.contatos_routes import get_contato

usuario_bp = Blueprint('usuarios', __name__)
permitidos = ["admin", "usuario"]

@usuario_bp.route("/cadastro-usuarios", methods=["POST"])
def cadastro_usuario():
    dados = request.get_json()
    if not dados:
        return resp_erro("Json invalido!", 400)
    
    username = dados["username"]
    password = generate_password_hash(dados["password"])
    cargo = "usuario"

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO  usuario (username, password, cargo) values (?,?,?)""", (username, password,cargo))

    conn.commit()
    cursor.close()
    conn.close()

    return resp_sucess("usuario criado com sucesso", 200)

@usuario_bp.route("/login", methods=["POST"])
def login():
    dados = request.get_json()
    if not dados:
        return resp_erro("Json invalido!", 400)
    
    username = dados["username"]
    password = dados["password"]

    
    if not username or not password:
        return resp_erro("Campos Obrigatorios", 400)
    
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, username, password, cargo from usuario where username= ?", (username,))
    usuarios = cursor.fetchone()
    
    cursor.close()
    conn.close()

    if not usuarios:
        return resp_erro("Usuario não encontrado!", 401)
    
    if not check_password_hash(usuarios[2], password):
        return resp_erro("Senha incorreta!", 401)
    session["usuario_id"] = usuarios[0]
    session["usuario"] = usuarios[1]
    session["cargo"] = usuarios[3]

    if session["cargo"] == "admin":
        return resp_sucess("admin entrou", 200)
    else:
        return resp_sucess("usuario entrou", 200) 

@usuario_bp.route("/lista-usuarios", methods=["GET"])
def lista_usuarios():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
    if session["cargo"] not in permitidos:
        return resp_erro("Acesso negado", 403)

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("select id, username, cargo from usuario")
    usuario = cursor. fetchall()
    return resp_sucess(usuario, 200)
    cursor.close()
    conn.close()
