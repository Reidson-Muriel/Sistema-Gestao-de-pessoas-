import re
from datetime import datetime, date

def validar_nome(nome):
    if not nome or len(nome.strip()) < 3:
        return False
    
    if nome.isdigit():
        return False
    
    if not re.match("^[A-Za-z]+$", nome):
        return "O nome não pode conter numero"
    
    return True

def validar_idade(idade):
    if idade is None:
        return True
    if not isinstance(idade,int):
        return False
    if idade < 0 or idade > 120:
        return False
    else:
        return True

def validar_telefone(telefone):
    if not telefone:
        return False
    if not telefone.isdigit():
        return False
    if len(telefone) != 11:
        return False
    else:
        return True
def validar_email(email):
    if not email:
        return True
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return True
    else:
        return False
    
def calcular_idade(nascimento:date):
    if not nascimento:  
        return None
    try:
        if(isinstance(nascimento, str)):
            nascimento = datetime.strptime(nascimento, "%Y-%m-%d").date()
        atual = date.today()
        idade = atual.year - nascimento.year
        if (atual.month, atual.day) < (nascimento.month, nascimento.day):
            idade -=1
        return idade
    except Exception:
        return None