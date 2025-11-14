import json
import os
from datetime import datetime
import time
from typing import List

from model.usuario_model import Usuario
from model.perfil_model import Perfil
from model.funcao_model import Funcao

import uteis.conexao_mysql as Conexao_mysql
from uteis.app_config import App_config

class Perfil_dao:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

    def listar_perfis(self, conexao_bd : Conexao_mysql, perfil_filtro : Perfil=None) -> List[Perfil]:
        
        perfis : List[Perfil] = None

        consulta = """
            SELECT cd_perfil, nm_perfil
            FROM tb_perfil per
            WHERE 1=1
        """
        if perfil_filtro != None :
            consulta += " AND per.cd_perfil = " + str(perfil_filtro.codigo)
        
        consulta += " ORDER BY per.nm_perfil "
        resultados = conexao_bd.consultar_sql(consulta)

        if resultados != None:
            perfis = []
            for resultado in resultados:
                perfis.append(Perfil(resultado[0], resultado[1]))
        
        return perfis
    