import os

from uteis.app_config import App_config
from uteis.conexao_mysql import Conexao_mysql

    

class Controller:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

        self._app_config.carregar_config()

        self._conexao_bd = Conexao_mysql(
                            self._app_config.pegar_valor('db_host'), 
                            self._app_config.pegar_valor('db_port'), 
                            self._app_config.pegar_valor('db_user'), 
                            self._app_config.pegar_valor('db_pass'), 
                            self._app_config.pegar_valor('db_name') )
    
    @property
    def conexao_bd(self)->Conexao_mysql:
        return self._conexao_bd

    @conexao_bd.setter
    def conexao_bd(self, value : Conexao_mysql):
        self._conexao_bd = value

    @conexao_bd.deleter
    def conexao_bd(self):
        del self._conexao_bd


    #################################################

    @property
    def app_config(self)->App_config:
        return self._app_config

    @app_config.setter
    def app_config(self, value : App_config):
        self._app_config = value

    @app_config.deleter
    def app_config(self):
        del self._app_config

