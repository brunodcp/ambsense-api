import json
from datetime import datetime
import time

import uteis.json as json_uteis

from model.leitura_model import Leitura

class Sensor:
    def __init__(self,
                 codigo : int = 0, 
                 descricao : str = "", 
                 parametro : str = "", 
                 leituras : Leitura = []) :
        self.codigo : str = codigo
        self.descricao : str = descricao
        self.parametro : str = parametro
        self.leituras : Leitura = leituras

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("descricao", self.descricao) +','
        str_json += json_uteis.chave_valor_to_json("parametro", self.parametro) +','
        str_json += '''"leituras":['''
        for idx, leitura in enumerate(self.leituras) :
            str_json += leitura.to_json()
            if idx < len(self.leituras)-1 : str_json += ''','''
        str_json += ''']'''
        str_json += '''}'''

        return str_json