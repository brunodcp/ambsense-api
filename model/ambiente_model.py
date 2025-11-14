import json
from datetime import datetime
import time

import uteis.json as json_uteis

from model.dispositivo_model import Dispositivo

class Ambiente:
    def __init__(self,
                 codigo : int = 0, 
                 descricao : str = "", 
                 wifi : str = "",
                 senha_wifi : str = "",
                 dispositivos : Dispositivo = [],
                 ordem : int = 0) :
        
        self.codigo : str = codigo
        self.descricao : str = descricao
        self.wifi : str = wifi
        self.senha_wifi : str = senha_wifi
        self.dispositivos : Dispositivo = dispositivos
        self.ordem : int = ordem

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("descricao", self.descricao) +','
        str_json += json_uteis.chave_valor_to_json("wifi", self.wifi) +','
        str_json += json_uteis.chave_valor_to_json("senha_wifi", self.senha_wifi) +','
        str_json += '''"dispositivos":['''
        for idx, dispositivo in enumerate(self.dispositivos) :
            str_json += dispositivo.to_json()
            if idx < len(self.dispositivos)-1 : str_json += ''','''
        str_json += '''],'''
        str_json += json_uteis.chave_valor_to_json("ordem", self.ordem)
        str_json += '''}'''

        return str_json