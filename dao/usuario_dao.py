import json
from datetime import datetime
import time
from typing import List
from uuid import uuid4


from model.perfil_model import Perfil
from model.usuario_model import Usuario
from model.ambiente_model import Ambiente

import uteis.conexao_mysql as Conexao_mysql
from uteis.app_config import App_config



class Usuario_dao:
    def __init__(self):
        pass

    def listar(self, conexao_bd : Conexao_mysql, usuario_filtro : Usuario) -> List[Usuario]:
        usuarios : List[Usuario] = None

        consulta = """
            SELECT usu.cd_usuario, usu.nm_usuario, usu.dc_email, usu.dc_senha, 
                    per.cd_Perfil, per.nm_Perfil, 
                    usu.dc_firebase_token, usu.dt_firebase_token,
                    usu.dc_ticket_troca_senha, usu.dt_ticket_troca_senha, usu.in_ativo    
            FROM tb_usuario usu
            JOIN tb_perfil per ON (usu.cd_Perfil = per.cd_Perfil) 
            WHERE 1=1 
        """
        if usuario_filtro != None :
            if (usuario_filtro.codigo != '0') : 
                consulta += "  AND cd_usuario = '" + str(usuario_filtro.codigo) + "'"
            if (usuario_filtro.email != None and usuario_filtro.email != "") : 
                consulta += "  AND UCASE(dc_email) = UCASE('" + usuario_filtro.email + "') "
            if (usuario_filtro.senha != None and usuario_filtro.senha != "") : 
                consulta += "  AND dc_senha = '" + usuario_filtro.senha + "'"
            if (usuario_filtro.ticket_troca_senha != None and usuario_filtro.ticket_troca_senha != "") : 
                consulta += "  AND dc_ticket_troca_senha = '" + usuario_filtro.ticket_troca_senha + "'" 
                consulta += "  AND (dt_Ticket_Troca_Senha IS NULL OR dt_Ticket_Troca_Senha >= DATE_ADD(NOW(), INTERVAL -7 DAY) )" 
        consulta += " ORDER BY usu.nm_usuario "
        
        resultados = conexao_bd.consultar_sql(consulta)

        if resultados != None:
            usuarios = []
            for resultado in resultados:
                print(resultado[0])
                usuarios.append(Usuario(resultado[0], resultado[1], resultado[2], resultado[3],
                                        Perfil(resultado[4], resultado[5]), True,
                                        resultado[6], resultado[7],
                                        resultado[8], resultado[9], (resultado[10]=='S'), []))
        
        return usuarios

    def salvar (self, conexao_bd : Conexao_mysql, usuario :Usuario) -> Usuario:
        usuario_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if usuario.codigo == '0':
                usuario.codigo = str(uuid4())
                script = f"""
                    INSERT INTO tb_usuario(cd_usuario, nm_usuario, dc_email, cd_Perfil, dc_Senha, dc_ticket_troca_senha)
                    VALUES('{usuario.codigo}', '{usuario.nome}', '{usuario.email}', {usuario.perfil.codigo}, '{usuario.senha}', '{usuario.ticket_troca_senha}')"""
                cursor.execute(script, None)
                if (cursor.rowcount == 1):
                    print("Fez o insert " + script )
                    usuario_salvo = usuario

            else:

                script = f"""
                    UPDATE tb_usuario
                    SET nm_usuario = '{usuario.nome}'
                    ,    dc_email = '{usuario.email}'
                    ,    cd_Perfil = '{usuario.perfil.codigo}'
                    WHERE cd_usuario = '{usuario.codigo}' """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o update " + script )
                    usuario_salvo = usuario
                else:
                    print("Não fez o update " + script )
                usuario_salvo = usuario
        except Exception as ex:
            print(str(ex))

        return usuario_salvo
    
    def excluir (self, conexao_bd : Conexao_mysql, usuario :Usuario) -> Usuario:
        usuario_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if usuario.codigo != '0' and usuario.codigo != None and usuario.codigo != '':
            
                script = f"""
                    DELETE FROM tb_usuario
                    WHERE cd_usuario = '{usuario.codigo}' """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o delete " + script )
                    usuario_salvo = usuario
                else:
                    print("Não fez o delete " + script )
                usuario_salvo = usuario
        except Exception as ex:
            print(str(ex))

        return usuario_salvo

    def trocar_senha (self, conexao_bd : Conexao_mysql, usuario :Usuario) -> Usuario:
        usuario_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if usuario.codigo != '0':
                script = f"""
                    UPDATE tb_usuario
                    SET dc_senha = '{usuario.senha}'
                    ,   dc_ticket_troca_senha = NULL
                    ,   dt_ticket_troca_senha = NULL
                    WHERE cd_usuario = '{usuario.codigo}'
                      AND dc_ticket_troca_senha = '{usuario.ticket_troca_senha}'
                      AND (dt_Ticket_Troca_Senha IS NULL OR dt_Ticket_Troca_Senha >= DATE_ADD(NOW(), INTERVAL -7 DAY) ) """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o update " + script )
                    usuario_salvo = usuario
                else:
                    print("Não fez o update " + script )
                usuario_salvo = usuario
        except Exception as ex:
            print(str(ex))

        return usuario_salvo

    def resetar_senha (self, conexao_bd : Conexao_mysql, usuario :Usuario) -> Usuario:
        usuario_salvo = None
        try:
            cursor = conexao_bd.cursor()
            if usuario.codigo != '0':
                script = f"""
                    UPDATE tb_usuario
                    SET dc_ticket_troca_senha = '{usuario.ticket_troca_senha}'
                    ,   dt_ticket_troca_senha = Now()
                    WHERE dc_email = '{usuario.email}' """
                cursor.execute(script)
                if (cursor.rowcount == 1):
                    print("Fez o update " + script )
                    usuario_salvo = usuario
                else:
                    print("Não fez o update " + script )
                usuario_salvo = usuario
        except Exception as ex:
            print(str(ex))

        return usuario_salvo