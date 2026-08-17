from sistema.utils.response import resp_erro, resp_sucess
from flask import Blueprint, jsonify, request, session
from sistema.models.contatos_model import adicionar_contato, atualizar_contatos, deletar_contatos
from sistema.services.contatos_services import obter_contatos, buscar_contatos_id

contato_bp = Blueprint('contato', __name__)

permitidos = ["admin", "usuario"]
#rotas para contatos mostrar todos cadastros
@contato_bp.route("/contatos", methods=["GET"])
def get_contato():
        
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    if session["cargo"] not in permitidos:
                return resp_erro("Acesso negado", 403)
    try:
        contato = obter_contatos(session["usuario_id"], session["cargo"])
        if not contato:
            return resp_erro("Nenhum contato encontrado", 404)
        return resp_sucess(contato, status=200)
    except Exception as e:
        return resp_erro("Erro ao buscar contatos " + str(e), 500)

# rotas para contato pelo id mostrar unico contatos
@contato_bp.route("/contatos/<int:id>", methods=["GET"])
def get_contato_id(id):
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    if session["cargo"] not in permitidos:
            return resp_erro("Acesso negado", 403)

    try:
        buscar = buscar_contatos_id(id, session["usuario_id"], session["cargo"])
        if not buscar:
            return resp_erro("Contato nao encontrado", 404)

        return resp_sucess(buscar, status=200)
    except Exception as e:
        return resp_erro("Erro ao buscar contato " + str(e), 500)
# criar rota para adicionar contato read
@contato_bp.route("/contatos", methods=["POST"])
def criar_contato():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    if session["cargo"] not in permitidos:
        return resp_erro("Acesso negado", 403)
    try:
        dados = request.get_json()
        if not dados:
            return resp_erro("dados invalidos", 400)

        logado_usuario_id = session["usuario_id"]
        contato_usuario_id = dados["usuario_id"]
        return adicionar_contato(dados, session["cargo"])
    except Exception as e:
        return resp_erro("Erro ao criar contato " + str(e), 500)
     
#rota para atualizar o contato read/update
@contato_bp.route("/contatos/<int:id>", methods=["PUT"])
def atualizar_contato(id): 
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
    
    if session["cargo"] not in permitidos:
        return resp_erro("Acesso negado", 403)
    
    try:
        dados = request.get_json(silent=True)

        if not dados:
            return resp_erro("Dados invalidos", 400)

        return atualizar_contatos(id, dados)
    except Exception as e:
        return resp_erro("Erro ao atualizar contato " + str(e), 500)

# rota para deletar o contato delete 
@contato_bp.route("/contatos/<int:id>", methods=["DELETE"])
def deletar_contato(id):
    usuario_id = session["usuario"]
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    if session["cargo"] not in permitidos:
        return resp_erro("Acesso negado", 403)
    try:
        return deletar_contatos(id, usuario_id)
    except Exception as erro:
        return resp_erro("Erro ao deletar o contato" + str(erro), 500)

@contato_bp.route("/me", methods=["GET"])
def usuario_logado():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    if session["cargo"] not in permitidos:
        return resp_erro("Acesso negado", 403)
    
    return resp_sucess({
        "usuario": session["usuario"],
        "cargo": session["cargo"]
    })    