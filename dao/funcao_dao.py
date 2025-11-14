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


class Funcao_dao:
    def __init__(self):
        self._app_config = App_config(os.path.join("config","config.json"))

    def listar_funcoes(self, conexao_bd : Conexao_mysql, perfil_filtro : Perfil, funcao_grupo : Funcao | None = None) -> List[Funcao]:
        
        funcoes : List[Funcao] = None

        consulta = """
          SELECT fun.cd_Funcao, fun.nm_Funcao, fun.dc_URL, fun.dc_Icone, 
                 fun.dc_Alias, fun.nr_Ordem,
                 pfu.in_Consultar, pfu.in_Incluir, pfu.in_Alterar, pfu.in_Excluir
          FROM tb_funcao fun
          JOIN tb_perfil_funcao pfu ON (fun.cd_Funcao = pfu.cd_Funcao) 
          WHERE pfu.cd_Perfil = """ + str(perfil_filtro.codigo)
        if (funcao_grupo != None):
            consulta += " AND cd_Funcao_Grupo = " + str(funcao_grupo.codigo)
        else:
            consulta += " AND cd_Funcao_Grupo IS NULL "
        consulta += " ORDER BY fun.nr_Ordem "
        
        resultados = conexao_bd.consultar_sql(consulta)
        if resultados != None:
            funcoes = []
            for resultado in resultados:
                funcoes.append(Funcao(resultado[0], resultado[1], resultado[2], resultado[3], 
                                      resultado[4], resultado[5], 
                                      (resultado[6]=='S'), (resultado[7]=='S'), (resultado[8]=='S'), (resultado[9]=='S') )
                            )
        
        return funcoes