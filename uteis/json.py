import time

def chave_valor_to_json(chave, valor):
    chave_valor = ""
    if valor == None:
        chave_valor = '"' + chave + '":null'
    elif isinstance(valor, bool) : #valor == True or valor == False :
        valor = str(valor).lower()
        chave_valor = '"' + chave + '":' + valor
    elif isinstance(valor, time.struct_time) :
        valor = time.strftime('%Y-%m-%dT%H:%M:%SZ', valor)
        chave_valor = '"' + chave + '":"' + valor + '"'
    elif isinstance(valor, int) or isinstance(valor, float) :
        valor = str(valor)
        chave_valor = '"' + chave + '":' + valor
    else : 
        valor = str(valor)
        valor = valor.replace("\\", r'\\')
        chave_valor = '"' + chave + '":"' + valor + '"'
    return str(chave_valor)

def valor_to_json(valor):
    if valor == None:
        valor = "null"
    elif isinstance(valor, bool) : #valor == True or valor == False :
        valor = str(valor).lower()
    elif isinstance(valor, time.struct_time) :
        valor = time.strftime('%Y-%m-%dT%H:%M:%SZ', valor)
    elif isinstance(valor, int) or isinstance(valor, float) :
        valor = str(valor)
    else : 
        valor = str(valor)
    return str(valor)