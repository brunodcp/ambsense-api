import json
from datetime import datetime
import time

import uteis.json as json_uteis

from model.ambiente_model import Ambiente

class Local:
    def __init__(self,
                 codigo : int = 0, 
                 descricao : str = "",
                 wifi : str = "",
                 senha_wifi : str = "",
                 fuso_horario : float = 0,
                 ambientes : Ambiente = [],
                 ordem : int = 0) :
        self.codigo : str = codigo
        self.descricao : str = descricao
        self.wifi : str = wifi
        self.senha_wifi : str = senha_wifi
        self.fuso_horario : float = fuso_horario
        self.ambientes : Ambiente = ambientes
        self.ordem : int = ordem

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("descricao", self.descricao) +','
        str_json += json_uteis.chave_valor_to_json("fuso_horario", self.fuso_horario) +','
        str_json += '''"ambientes":['''
        for idx, ambiente in enumerate(self.ambientes) :
            str_json += ambiente.to_json()
            if idx < len(self.ambientes)-1 : str_json += ''','''
        str_json += '''],'''
        str_json += json_uteis.chave_valor_to_json("ordem", self.ordem)
        str_json += '''}'''

        return str_json