## isso aqui e tudo no banco de dados SQL
from sistema.utils.logger import logger
from sistema.database import conexao
from sistema.utils.response import resp_sucess, resp_erro
from sistema.utils.validacao import validar_email, validar_idade, validar_nome, validar_telefone, calcular_idade
def listar_contatos():
    conection = conexao.conectar()
    cursor = conection.cursor()
    try:

        cursor.execute("select id, nome, telefone from contatos")
        dados = cursor.fetchall()


        return dados
    except Exception as e:
       raise e
    finally:
        cursor.close()
        conection.close()

def buscar_contato(id):
    conection = conexao.conectar()
    cursor = conection.cursor()
    try:
    
        cursor.execute("select id, nome, telefone, email, endereco, observacao, data_nascimento " \
                        "from contatos where id = ? ", (id,))
        dados = cursor.fetchone()
    
        return dados
    except Exception as e:
       raise e
    finally:           
        cursor.close()
        conection.close()

def adicionar_contato(dado):
    conection = conexao.conectar()
    cursor = conection.cursor()
    try:
        nome = dado.get("nome") 
        data_nascimento =  dado.get("data_nascimento")
        telefone = dado.get("telefone")
        email =  dado.get("email")
        endereco = dado.get("endereco")
        observacao = dado.get("observacao")

        if not nome or not telefone:
            return resp_erro("Nome e telefone sao obrigatorios", 400)
        
        if not validar_nome(nome):
            return resp_erro("Nome invalido, deve ter pelo menos 3 caracteres em letras", 400)

        
        if not validar_telefone(telefone):
            return resp_erro("Telefone invalido, deve conter apenas numeros de 11 digitos", 400)
        
        if not validar_email(email):
            return resp_erro("Email invalido", 400)

        


        cursor.execute("select id from contatos where telefone= ?", (telefone,))#evitar o telefone duplas
        existe = cursor.fetchone()
        if existe:
            cursor.close()
            conection.close()
            return resp_erro("contato ja existe", 409)
        else:
            cursor.execute("insert into contatos (nome, telefone, email, endereco, observacao, data_nascimento) " \
                           "values (?,?,?,?,?,?)",(nome, telefone, email or None, endereco or None, observacao or None,  data_nascimento))
            conection.commit()

            return resp_sucess("Contato criado com sucesso", 201)
    except Exception as e:
        logger.error(f"Erro ao adicionar contato: {e}")
        raise e

    finally:
        cursor.close()
        conection.close()

def atualizar_contatos(id, dado):
    conection = conexao.conectar()
    cursor = conection.cursor() 
    try:

        cursor.execute("""select nome, telefone, email, endereco, observacao, data_nascimento from contatos
                       where id=?""", (id,))

        contato = cursor.fetchone()
        if contato:
            nome = dado.get("nome", contato[0])
            telefone_novo = dado.get("telefone", contato[1])
            email = dado.get("email", contato[2])
            endereco = dado.get("endereco", contato[3])
            observacao = dado.get("observacao", contato[4])
            data_nascimento = dado.get("nascimento", contato[5])

            if not validar_nome(nome):
                return resp_erro("Nome invalido", 400)
            
            if not validar_telefone(telefone_novo):
                return resp_erro("Telefone invalido", 400)

            if not validar_email(email):
                return resp_erro("Email invalido", 400)
            
            cursor.execute("""update contatos set nome=?, telefone=?, email=?, endereco=?, observacao=?, data_nascimento=? 
                           where id=?""", (nome, telefone_novo, email, endereco, observacao, data_nascimento, id))
            conection.commit()

            return resp_sucess("Contato atualizado com sucesso", 200)
        else:
            cursor.close()
            conection.close() 
            return resp_erro("Contato nao encontrado", 404)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conection.close()
   
def deletar_contatos(id):
    conection = conexao.conectar()
    cursor = conection.cursor()
    try:

        cursor.execute("select id from contatos where id=?", (id,))
        existe = cursor.fetchone()

        if existe:
            cursor.execute("delete from contatos where id=?", (id,))
            conection.commit()
            cursor.close()
            conection.close()
            return resp_sucess("contato deletado com sucesso", 200)
        else:
            return resp_erro("Contato nao encontrado", 404)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conection.close()
        

