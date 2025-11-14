import json
from datetime import datetime
import time

import uteis.json as json_uteis

class Funcao:
    def __init__(self,
                 codigo : int = 0, 
                 nome : str = "", 
                 url : str = "", 
                 icone : str = "", 
                 alias : str = "", 
                 ordem : int = 0,
                 pode_consultar : bool = False,
                 pode_incluir : bool = False,
                 pode_alterar : bool = False,
                 pode_excluir : bool = False) :
        
        self.codigo : int = codigo
        self.nome : str = nome
        self.url : str = url
        self.icone : str = icone
        self.alias : str = alias
        self.ordem : str = ordem

        self.pode_consultar : bool = pode_consultar
        self.pode_incluir : bool = pode_incluir
        self.pode_alterar : bool = pode_alterar
        self.pode_excluir : bool = pode_excluir

    def to_json(self) : 
        
        str_json = '''{'''
        str_json += json_uteis.chave_valor_to_json("codigo", self.codigo) +','
        str_json += json_uteis.chave_valor_to_json("nome", self.nome) +','
        str_json += json_uteis.chave_valor_to_json("url", self.url) +','
        str_json += json_uteis.chave_valor_to_json("icone", self.icone) +','
        str_json += json_uteis.chave_valor_to_json("alias", self.alias) +','
        str_json += json_uteis.chave_valor_to_json("ordem", self.ordem) +','
        str_json += json_uteis.chave_valor_to_json("pode_consultar", self.pode_consultar) +','
        str_json += json_uteis.chave_valor_to_json("pode_incluir", self.pode_incluir) +','
        str_json += json_uteis.chave_valor_to_json("pode_alterar", self.pode_alterar) +','
        str_json += json_uteis.chave_valor_to_json("pode_excluir", self.pode_excluir)
        str_json += '''}'''

        return str_json