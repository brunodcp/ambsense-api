import json
from datetime import datetime
import time

import uteis.json as json_uteis

class Controle:
    def __init__(self,
                 codigo : int = 0, 
                 tipo : str = "", 
                 descricao : str = "", 
                 valor : str = "", 
                 alterado_em : datetime = "", 
                 acao : str = "") :
        
        self.codigo : str = codigo
        self.tipo : str = tipo
        self.descricao : str = descricao
        self.valor :str = valor
        self.alterado_em : datetime = alterado_em 
        self.acao : str = acao

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("tipo", self.tipo) +','
        str_json += json_uteis.chave_valor_to_json("descricao", self.descricao) +','
        str_json += json_uteis.chave_valor_to_json("valor", self.valor) +','
        str_json += json_uteis.chave_valor_to_json("alterado_em", self.alterado_em) +','
        str_json += json_uteis.chave_valor_to_json("acao", self.acao) +','
        str_json += '''}'''

        return str_json