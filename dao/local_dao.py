import json
import os
from datetime import datetime
import time
from typing import List

from model.usuario_model import Usuario
from model.local_model import Local




import uteis.conexao_mysql as Conexao_mysql
from uteis.app_config import App_config


class Local_dao:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

    def listar_locais(self, conexao_bd : Conexao_mysql, usuario : Usuario, local_filtro : Local=None) -> List[Local]:
        
        locais : List[Local] = None

        consulta = """
            SELECT cd_Local, dc_Local, dc_Wifi, dc_Senha_Wifi, 
                    vl_FusoHorario, nr_Ordem
            FROM tb_local per
            WHERE per.cd_usuario = """ + str(usuario.codigo)
        
        if local_filtro != None :
            consulta += " AND per.cd_local = " + str(local_filtro.codigo)

        consulta += " ORDER BY per.nr_ordem "
        resultados = conexao_bd.consultar_sql(consulta)

        if resultados != None:
            locais = []
            for resultado in resultados:
                locais.append(Local(resultado[0], resultado[1], resultado[2], resultado[3], 
                                    resultado[4], [], resultado[5] ))
        
        return locais
    
