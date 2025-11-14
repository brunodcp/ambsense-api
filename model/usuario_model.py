import json
from datetime import datetime
import time
from typing import List

import uteis.json as json_uteis

from model.perfil_model import Perfil
from model.local_model import Local

class Usuario:
    
    def __init__(self, 
                 codigo:int = 0, 
                 nome:str = "", 
                 email:str = "", 
                 senha : str = "", 
                 perfil : Perfil = None, 
                 autenticado: bool = False, 
                 firebase_token : str = "",
                 data_firebase_token : datetime = None,
                 ticket_troca_senha: str = "", 
                 data_ticket_troca_senha : datetime = None, 
                 ativo:bool = False, 
                 locais : List[Local] = [] ):

        self._codigo : int = codigo 
        self._nome : str = nome
        self._email : str = email
        self._senha : str = senha
        self._perfil : Perfil = perfil
        self._autenticado: bool = autenticado
        self._firebase_token : str = firebase_token
        self._data_firebase_token : datetime = data_firebase_token
        self._ticket_troca_senha: str = ticket_troca_senha
        self._data_ticket_troca_senha : datetime = data_ticket_troca_senha
        self._ativo : bool = ativo
        self._locais : List[Local] = locais
    
    ############ codigo
    @property
    def codigo(self)->str: return self._codigo
    @codigo.setter
    def codigo(self, value : str): self._codigo = value
    @codigo.deleter
    def conexao_bd(self): del self._codigo


    ############ nome
    @property
    def nome(self)->str: return self._nome
    @nome.setter
    def nome(self, value : str): self._nome = value
    @nome.deleter
    def nome(self): del self._nome

    ############ email
    @property
    def email(self)->str: return self._email
    @nome.setter
    def email(self, value : str): self._email = value
    @email.deleter
    def email(self): del self._email

    ############ senha
    @property
    def senha(self)->str: return self._senha
    @senha.setter
    def senha(self, value : str): self._senha = value
    @senha.deleter
    def senha(self): del self._senha

    ############ perfil
    @property
    def perfil(self)->Perfil: return self._perfil
    @perfil.setter
    def perfil(self, value : Perfil): self._perfil = value
    @perfil.deleter
    def perfil(self): del self._perfil

    ############ autenticado
    @property
    def autenticado(self)->bool: return self._autenticado
    @autenticado.setter
    def autenticado(self, value : bool): self._autenticado = value
    @autenticado.deleter
    def autenticado(self): del self._autenticado

    ############ firebase_token
    @property
    def firebase_token(self)->str: return self._firebase_token
    @firebase_token.setter
    def firebase_token(self, value : str): self._firebase_token = value
    @firebase_token.deleter
    def firebase_token(self): del self._firebase_token

    ############ data_firebase_token
    @property
    def data_firebase_token(self)->datetime: return self._data_firebase_token
    @data_firebase_token.setter
    def data_firebase_token(self, value : datetime): self._data_firebase_token = value
    @data_firebase_token.deleter
    def data_firebase_token(self): del self._data_firebase_token

    ############ ticket_troca_senha
    @property
    def ticket_troca_senha(self)->str: return self._ticket_troca_senha
    @ticket_troca_senha.setter
    def ticket_troca_senha(self, value : str): self._ticket_troca_senha = value
    @ticket_troca_senha.deleter
    def ticket_troca_senha(self): del self._ticket_troca_senha

    ############ data_ticket_troca_senha
    @property
    def data_ticket_troca_senha(self)->datetime: return self._data_ticket_troca_senha
    @data_ticket_troca_senha.setter
    def data_ticket_troca_senha(self, value : datetime): self._data_ticket_troca_senha = value
    @data_ticket_troca_senha.deleter
    def data_ticket_troca_senha(self): del self._data_ticket_troca_senha

    ############ ativo
    @property
    def ativo(self)->bool: return self._ativo
    @ativo.setter
    def ativo(self, value : bool): self._ativo = value
    @ativo.deleter
    def ativo(self): del self._ativo

    ############ locais
    @property
    def locais(self)->List[Local]: return self._locais
    @locais.setter
    def locais(self, value : List[Local]): self._locais = value
    @locais.deleter
    def locais(self): del self._locais

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("nome", self.nome) +','
        str_json += json_uteis.chave_valor_to_json("email", self.email) +','
        str_json += json_uteis.chave_valor_to_json("senha", self.senha) +','
        str_json += '"perfil":' + self.perfil.to_json() + ','
        str_json += json_uteis.chave_valor_to_json("autenticado", self.autenticado) +','
        str_json += json_uteis.chave_valor_to_json("firebase_token", self.firebase_token) +','
        str_json += json_uteis.chave_valor_to_json("data_firebase_token", self.data_firebase_token) +','
        str_json += json_uteis.chave_valor_to_json("ticket_troca_senha", self.ticket_troca_senha) +','
        str_json += json_uteis.chave_valor_to_json("data_ticket_troca_senha", self.data_ticket_troca_senha) +','
        str_json += json_uteis.chave_valor_to_json("ativo", self.ativo) +','
        str_json += '"locais":['
        for idx, local in enumerate(self.locais) :
            str_json += local.to_json()
            if idx < len(self.locais)-1 : str_json += ','
        str_json += ']'
        str_json += '''}'''

        return str_json