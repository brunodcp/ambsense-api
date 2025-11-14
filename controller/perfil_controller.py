import json
import os
from datetime import datetime
import time
from typing import List

from model.perfil_model import Perfil
from model.funcao_model import Funcao

from dao.perfil_dao import Perfil_dao

from uteis.app_config import App_config
from uteis.conexao_mysql import Conexao_mysql

class Perfil_controller:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

        self._app_config.carregar_config()

        self._conexao_bd = Conexao_mysql(
                            self._app_config.pegar_valor('db_host'), 
                            self._app_config.pegar_valor('db_port'), 
                            self._app_config.pegar_valor('db_user'), 
                            self._app_config.pegar_valor('db_pass'), 
                            self._app_config.pegar_valor('db_name') )


    def listar_perfis(self, perfil_filtro : Perfil=None) -> List[Perfil] | None:
        perfis = None
        perfil_dao = Perfil_dao()

        if self._conexao_bd.conectar():
            
            perfis = perfil_dao.listar_perfis(self._conexao_bd, perfil_filtro)
            
            self._conexao_bd.fechar()
        
        return perfis
    
    def listar_funcoes(self, perfil_filtro : Perfil, funcao_grupo : Funcao = None) -> List[Funcao] | None:
        funcoes : List[Funcao] = None
        perfil_dao : Perfil_dao = Perfil_dao()

        if self._conexao_bd.conectar():
            
            funcoes = perfil_dao.listar_funcoes(self._conexao_bd, perfil_filtro, funcao_grupo)
            
            self._conexao_bd.fechar()
        
        return funcoes