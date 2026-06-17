from sistema.utils.response import resp_sucess, resp_erro
from flask import Blueprint, jsonify, request, session
from sistema.models.contatos_model import adicionar_contato, atualizar_contatos, deletar_contatos
from sistema.services.contatos_services import obter_contatos, buscar_contatos_id

contato_bp = Blueprint('contato',__name__)

#rotas para contatos mostrar todos cadastros
@contato_bp.route("/contatos", methods=["GET"])
def get_contato():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
    try:
        contato = obter_contatos(session["usuario"], session["cargo"])
        if contato:
            return resp_sucess(contato, status=200)
        else:
            return resp_erro("Nenhum contato encontrado", 404)
    except Exception as e:
        return resp_erro("Erro ao buscar contatos " + str(e), 500)
    
# rotas para contato pelo id mostrar unico contatos
@contato_bp.route("/contatos/<int:id>", methods=["GET"])
def get_contato_id(id):
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
    try:
        buscar = buscar_contatos_id(id, session["usuario"], session["cargo"])
        if buscar:
            return resp_sucess(buscar, status=200)
        else:
            return resp_erro("Contato nao encontrado", 404)
    except Exception as e:
        return resp_erro("Erro ao buscar contato " + str(e), 500)
# criar rota para adicionar contato read
@contato_bp.route("/contatos", methods=["POST"])
def criar_contato():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
    try:
        dados = request.get_json()
        if not dados:
            return resp_erro("dados invalidos", 400)

        dados["usuario_id"] = session["usuario"]
        
        return adicionar_contato(dados)
    except Exception as e:
        return resp_erro("Erro ao criar contato " + str(e), 500)
     
#rota para atualizar o contato read/update
@contato_bp.route("/contatos/<int:id>", methods=["PUT"])
def atualizar_contato(id):  
    if session["cargo"] != "admin":
        return resp_erro("Acesso negado", 403)
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)
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
    if session["cargo"] != "admin":
        return resp_erro("Acesso negado", 403)
    try:
        print("entrou no delete, indo para model...")
        return deletar_contatos(id, usuario_id)
    except Exception as erro:
        print("erro real:", erro)
        return resp_erro("Erro ao deletar o contato" + str(erro), 500)

@contato_bp.route("/me", methods=["GET"])
def usuario_logado():
    if "usuario" not in session:
        return resp_erro("Não autorizado", 401)

    return resp_sucess({
        "usuario": session["usuario"],
        "cargo": session["cargo"]
    })    