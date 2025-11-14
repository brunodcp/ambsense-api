import json
from datetime import datetime
import time

import uteis.json as json_uteis

from model.funcao_model import Funcao

class Perfil:
    def __init__(self,
                 codigo : int = 0, 
                 nome : str = "", 
                 funcoes : Funcao = []) :
        self.codigo : str = codigo
        self.nome : str = nome
        self.funcoes : Funcao = funcoes

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("nome", self.nome) +','
        str_json += '''"funcoes":['''
        for idx, funcao in enumerate(self.funcoes) :
            str_json += funcao.to_json()
            if idx < len(self.funcoes)-1 : str_json += ''','''
        str_json += ''']'''
        str_json += '''}'''

        return str_json