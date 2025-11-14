import json
from datetime import datetime
import time

import uteis.json as json_uteis



class Leitura:
    def __init__(self,
                 valor : str = 0, 
                 ip_request : str = "", 
                 ip_local : str = "", 
                 data : datetime = None) :
        
        self.valor : str = valor
        self.ip_request : str = ip_request
        self.ip_local : str = ip_local
        self.data : datetime = data

    def to_json(self) : 
        
        str_json = '{'
        str_json += json_uteis.chave_valor_to_json("valor", self.valor) +','
        str_json += json_uteis.chave_valor_to_json("ip_request", self.ip_request) +','
        str_json += json_uteis.chave_valor_to_json("ip_local", self.ip_local) +','
        str_json += json_uteis.chave_valor_to_json("data", self.data) +','
        str_json += '}'

        return str_json