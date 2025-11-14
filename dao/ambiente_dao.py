import json
import os
from datetime import datetime
import time
from typing import List

from model.usuario_model import Usuario
from model.ambiente_model import Ambiente
from model.local_model import Local



import uteis.conexao_mysql as Conexao_mysql
from uteis.app_config import App_config


class Ambiente_dao:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

    def listar_ambientes(self, conexao_bd : Conexao_mysql, usuario : Usuario, local_filtro : Local=None, ambiente_filtro : Ambiente=None) -> List[Ambiente]:
        
        ambientes : List[Ambiente] = None

        consulta = """
            SELECT amb.cd_ambiente, amb.dc_ambiente, amb.dc_wifi, amb.dc_senha_wifi, amb.nr_ordem
            FROM tb_ambiente amb
            JOIN tb_local loc ON (amb.cd_local = loc.cd_local)
            WHERE loc.cd_usuario = """ + str(usuario.codigo)
        
        if local_filtro != None :
            consulta += " AND amb.cd_local = " + str(local_filtro.codigo)

        if ambiente_filtro != None :
            consulta += " AND amb.cd_ambiente = " + str(ambiente_filtro.codigo)
        consulta += " ORDER BY amb.dc_ambiente "
        resultados = conexao_bd.consultar_sql(consulta)

        if resultados != None:
            ambientes = []
            for resultado in resultados:
                ambientes.append(Ambiente(resultado[0], resultado[1], resultado[2], resultado[3], 
                                    [], resultado[4] ))
        
        return ambientes
    