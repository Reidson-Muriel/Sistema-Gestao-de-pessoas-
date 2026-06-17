from sistema.models.contatos_model import listar_contatos, buscar_contato
from sistema.utils.response import resp_erro
from sistema.utils.logger import logger
from datetime import datetime

from ..utils.validacao import calcular_idade

def obter_contatos(usuario_id, cargo):
    try:
        contato = listar_contatos(usuario_id, cargo)

        lista = []
        for dados in contato:
            lista.append({"id": dados[0],
                          "nome": dados[1],
                          "telefone": dados[2]})
        return lista
    except Exception as e:
       raise e

def buscar_contatos_id(id, usuario_id, cargo):
    try:
        dados = buscar_contato(id, usuario_id, cargo)

        if not dados:
            return None

        data_nascimento = dados[6]
        if not data_nascimento:
            data_formatada = None
            idade = None
        else:
            data_formatada = data_nascimento
            idade = calcular_idade(data_formatada)

        contato = {
            "id": dados[0],
            "nome": dados[1],
            "telefone": dados[2],
            "email": dados[3],
            "endereco": dados[4],
            "observacao": dados[5],
            "data_nascimento": data_formatada,
            "idade": idade
        }

        return contato

    except Exception as e:
        logger.error(f"Erro ao buscar contato: {e}")
        resp_erro("Erro interno ao processar o contato")
