from werkzeug.security import generate_password_hash, check_password_hash
from flask import session
from flask import Blueprint, request
from sistema.utils.response import resp_sucess, resp_erro
from sistema.database.conexao import conectar

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route("/cadastro-usuarios", methods=["POST"])
def cadastro_usuario():
    dados = request.get_json()
    
    username = dados["username"]
    password = generate_password_hash(dados["password"])

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO  usuario (username, password) values (?,?)""", (username, password))

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

    cursor.execute("SELECT username, password from usuario where username = ?", (username,))
    usuarios = cursor.fetchone()
    
    cursor.close()
    conn.close()


    if not usuarios:
        return resp_erro("Usuario não encontrado!", 401)
    
    if not check_password_hash(usuarios[1], password):
        return resp_erro("Senha incorreto!", 401)
    session["usuario"] = username
    return resp_sucess("Login realizado com sucesso", 200)