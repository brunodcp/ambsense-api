import json
from datetime import datetime
import time

import uteis.json as json_uteis

from model.sensor_model import Sensor
from model.controle_model import Controle

class Dispositivo:
    def __init__(self,
                 codigo : int = 0, 
                 nome : str = "",
                 tipo : str = "",
                 ip_local : str = "",
                 ip_request : str = "",
                 wifi : str = "",
                 senha_wifi : str = "",
                 serial : str = "",
                 alarme : str = "",
                 data_criacao : datetime = None,
                 ativo : bool = False,
                 sensores : Sensor = [],
                 controles : Controle = []) :
        
        self.codigo : str = codigo
        self.nome : str = nome
        self.tipo : str = tipo,
        self.ip_local : str = ip_local
        self.ip_request : str = ip_request
        self.wifi : str = wifi
        self.senha_wifi : str = senha_wifi
        self.serial : str = serial
        self.alarme : str = alarme
        self.data_criacao : datetime = data_criacao
        self.ativo : bool = ativo
        self.sensores : Sensor = sensores
        self.controles : Controle = controles

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("nome", self.nome) +','
        str_json += json_uteis.chave_valor_to_json("tipo", self.tipo) +','
        str_json += json_uteis.chave_valor_to_json("ip_local", self.ip_local) +','
        str_json += json_uteis.chave_valor_to_json("ip_request", self.ip_request) +','
        str_json += json_uteis.chave_valor_to_json("wifi", self.wifi) +','
        str_json += json_uteis.chave_valor_to_json("senha_wifi", self.senha_wifi) +','
        str_json += json_uteis.chave_valor_to_json("serial", self.serial) +','
        str_json += json_uteis.chave_valor_to_json("alarme", self.alarme) +','
        str_json += json_uteis.chave_valor_to_json("data_criacao", self.data_criacao) +','
        str_json += json_uteis.chave_valor_to_json("ativo", self.ativo) +','
        str_json += '''"sensores":['''
        for idx, sensor in enumerate(self.sensores) :
            str_json += sensor.to_json()
            if idx < len(self.sensores)-1 : str_json += ''','''
        str_json += '''],'''
        str_json += '''"controles":['''
        for idx, controle in enumerate(self.controles) :
            str_json += controle.to_json()
            if idx < len(self.controles)-1 : str_json += ''','''
        str_json += ''']'''
        str_json += '''}'''

        return str_json