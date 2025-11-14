
import json
from datetime import datetime
import time
from typing import List
from uuid import uuid4


from model.perfil_model import Perfil
from model.dispositivo_model import Dispositivo
from model.ambiente_model import Ambiente

import uteis.conexao_mysql as Conexao_mysql
from uteis.app_config import App_config



class Dispositivo_dao:
    def __init__(self):
        pass

    def listar(self, conexao_bd : Conexao_mysql, dispositivo_filtro : Dispositivo) -> List[Dispositivo]:
        dispositivos : List[Dispositivo] = None

        consulta = """
            SELECT usu.cd_dispositivo, usu.nm_dispositivo, usu.dc_email, usu.dc_senha, 
                    per.cd_Perfil, per.nm_Perfil, 
                    usu.dc_firebase_token, usu.dt_firebase_token,
                    usu.dc_ticket_troca_senha, usu.dt_ticket_troca_senha, usu.in_ativo    
            FROM tb_dispositivo usu
            JOIN tb_perfil per ON (usu.cd_Perfil = per.cd_Perfil) 
            WHERE 1=1 
        """
        if dispositivo_filtro != None :
            if (dispositivo_filtro.codigo != '0') : 
                consulta += "  AND cd_dispositivo = '" + str(dispositivo_filtro.codigo) + "'"
            if (dispositivo_filtro.email != None and dispositivo_filtro.email != "") : 
                consulta += "  AND UCASE(dc_email) = UCASE('" + dispositivo_filtro.email + "') "
            if (dispositivo_filtro.senha != None and dispositivo_filtro.senha != "") : 
                consulta += "  AND dc_senha = '" + dispositivo_filtro.senha + "'"
            if (dispositivo_filtro.ticket_troca_senha != None and dispositivo_filtro.ticket_troca_senha != "") : 
                consulta += "  AND dc_ticket_troca_senha = '" + dispositivo_filtro.ticket_troca_senha + "'" 
                consulta += "  AND (dt_Ticket_Troca_Senha IS NULL OR dt_Ticket_Troca_Senha >= DATE_ADD(NOW(), INTERVAL -7 DAY) )" 
        consulta += " ORDER BY usu.nm_dispositivo "
        
        resultados = conexao_bd.consultar_sql(consulta)

        if resultados != None:
            dispositivos = []
            for resultado in resultados:
                print(resultado[0])
                dispositivos.append(Dispositivo(resultado[0], resultado[1], resultado[2], resultado[3],
                                        Perfil(resultado[4], resultado[5]), True,
                                        resultado[6], resultado[7],
                                        resultado[8], resultado[9], (resultado[10]=='S'), []))
        
        return dispositivos

    def salvar (self, conexao_bd : Conexao_mysql, dispositivo :Dispositivo) -> Dispositivo:
        dispositivo_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if dispositivo.codigo == '0':
                dispositivo.codigo = str(uuid4())
                script = f"""
                    INSERT INTO tb_dispositivo(cd_dispositivo, nm_dispositivo, dc_email, cd_Perfil, dc_Senha, dc_ticket_troca_senha)
                    VALUES('{dispositivo.codigo}', '{dispositivo.nome}', '{dispositivo.email}', {dispositivo.perfil.codigo}, '{dispositivo.senha}', '{dispositivo.ticket_troca_senha}')"""
                cursor.execute(script, None)
                if (cursor.rowcount == 1):
                    print("Fez o insert " + script )
                    dispositivo_salvo = dispositivo

            else:

                script = f"""
                    UPDATE tb_dispositivo
                    SET nm_dispositivo = '{dispositivo.nome}'
                    ,    dc_email = '{dispositivo.email}'
                    ,    cd_Perfil = '{dispositivo.perfil.codigo}'
                    WHERE cd_dispositivo = '{dispositivo.codigo}' """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o update " + script )
                    dispositivo_salvo = dispositivo
                else:
                    print("Não fez o update " + script )
                dispositivo_salvo = dispositivo
        except Exception as ex:
            print(str(ex))

        return dispositivo_salvo
    
    def excluir (self, conexao_bd : Conexao_mysql, dispositivo :Dispositivo) -> Dispositivo:
        dispositivo_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if dispositivo.codigo != '0' and dispositivo.codigo != None and dispositivo.codigo != '':
            
                script = f"""
                    DELETE FROM tb_dispositivo
                    WHERE cd_dispositivo = '{dispositivo.codigo}' """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o delete " + script )
                    dispositivo_salvo = dispositivo
                else:
                    print("Não fez o delete " + script )
                dispositivo_salvo = dispositivo
        except Exception as ex:
            print(str(ex))

        return dispositivo_salvo