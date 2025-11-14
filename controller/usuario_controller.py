from random import randrange
from typing import List
from uuid import uuid4

from controller.controller import Controller
from model.usuario_model import Usuario

from dao.usuario_dao import Usuario_dao
from dao.funcao_dao import Funcao_dao
from dao.local_dao import Local_dao
from dao.ambiente_dao import Ambiente_dao

#from uteis.app_config import App_config
#from uteis.conexao_mysql import Conexao_mysql

class Usuario_controller(Controller):
    def __init__(self):
        super().__init__()
    
    def validar_login_novo(self, usuario : Usuario=None) -> bool | None:
        validacao = None
        usuario_dao = Usuario_dao()

        if super().conexao_bd.conectar():
            
            usuarios = usuario_dao.listar(super().conexao_bd, usuario)
            
            if len(usuarios) > 0 : validacao = False
            else : validacao = True

            super().conexao_bd.fechar()
        
        return validacao

    def autenticar(self, usuario : Usuario) -> Usuario | None:
        
        usuario_autenticado = None
        usuario_dao = Usuario_dao()
        funcao_dao = Funcao_dao()
        local_dao = Local_dao()
        ambiente_dao = Ambiente_dao()

        if (usuario.email == None or usuario.email == ""):
            raise Exception(400, "E-mail não informado")
        elif (usuario.senha == None or usuario.senha == "") :
            raise Exception(400, "Senha não informada")
        else:
            if super().conexao_bd.conectar():    
                usuarios = usuario_dao.listar(super().conexao_bd, usuario)
                if (len(usuarios) == 1): 
                    usuario_autenticado = usuarios[0]
                    
                    if usuario_autenticado.perfil != None:
                        usuario_autenticado.perfil.funcoes = funcao_dao.listar_funcoes(super().conexao_bd, usuario_autenticado.perfil)
                    
                    usuario_autenticado.locais = local_dao.listar_locais(super().conexao_bd, usuario_autenticado)
                    if (len(usuario_autenticado.locais) > 0):
                        for idx_local, local in enumerate(usuario_autenticado.locais):
                            usuario_autenticado.locais[idx_local].ambientes = ambiente_dao.listar_ambientes(super().conexao_bd, usuario_autenticado, local)
                else:
                    super().conexao_bd.fechar()
                    raise Exception(400, "Usuário não autenticado")    
            
            super().conexao_bd.fechar()
            
        return usuario_autenticado
    
    def validar_ticket_troca_senha(self, usuario : Usuario) -> Usuario | None:
        
        usuario_validado = None
        usuario_dao = Usuario_dao()
        
        if (usuario.ticket_troca_senha == None or usuario.ticket_troca_senha == ""):
            raise Exception(400, "Ticket de troca de senha não informado")
        else:
            if super().conexao_bd.conectar():    
                usuarios = usuario_dao.listar(super().conexao_bd, usuario)
                if (len(usuarios) == 1): 
                    usuario_validado = usuarios[0]
                
            super().conexao_bd.fechar()
            
        return usuario_validado
    
    def gerar_senha(self) -> str:
        str_lib = "abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ0123456789!@$?_-"
        tamanho_senha = 5
        senha = ""
        for i in range(tamanho_senha):
            idx_random = randrange(len(str_lib))
            senha += str_lib[idx_random]
        return senha 
    
    def gerar_ticket_troca_senha(self) -> str:
        return "{" + str(uuid4()) + "}"

    def listar(self, usuario : Usuario) -> List[Usuario] | None:
        
        usuario_dao = Usuario_dao()
        usuarios : List[Usuario] = []
        if super().conexao_bd.conectar():    
            usuarios = usuario_dao.listar(super().conexao_bd, usuario)
             
            super().conexao_bd.fechar()
        
        return usuarios

    def salvar (self, usuario :Usuario) -> Usuario:
        usuario_dao = Usuario_dao()
        usuario_salvo: Usuario = None
        if (usuario.email == None or usuario.email == ""):
            raise Exception(400, "E-mail não informado")
        elif (usuario.senha == None or usuario.senha == "") :
            raise Exception(400, "Senha não informada")
        else:
            if super().conexao_bd.conectar():    
                usuario_salvo = usuario_dao.salvar(super().conexao_bd, usuario)
                super().conexao_bd.commit()
        return usuario_salvo
    
    def excluir (self, usuario :Usuario) -> Usuario:
        usuario_dao = Usuario_dao()
        usuario_salvo: Usuario = None
        if (usuario.codigo == None or usuario.codigo == ""):
            raise Exception(400, "Usuário não identificado")
        else:
            if super().conexao_bd.conectar():    
                usuario_salvo = usuario_dao.excluir(super().conexao_bd, usuario)
                super().conexao_bd.commit()
        return usuario_salvo
    
    def trocar_senha (self, usuario :Usuario) -> Usuario:
        usuario_dao = Usuario_dao()
        usuario_salvo: Usuario = None
        if (usuario.codigo == None or usuario.codigo == ""):
            raise Exception(400, "Usuário não identificado")
        elif (usuario.ticket_troca_senha == None or usuario.ticket_troca_senha == ""):
            raise Exception(400, "Ticket não informado")
        else:
            if super().conexao_bd.conectar():    
                usuario_salvo = usuario_dao.trocar_senha(super().conexao_bd, usuario)
                super().conexao_bd.commit()
        return usuario_salvo
    
    def resetar_senha (self, usuario :Usuario) -> Usuario:
        usuario_dao = Usuario_dao()
        usuario_salvo: Usuario = None
        if (usuario.email == None or usuario.email == ""):
            raise Exception(400, "E-mail não informado")
        else:
            if super().conexao_bd.conectar():    
                usuario.ticket_troca_senha = self.gerar_ticket_troca_senha()
                usuario_salvo = usuario_dao.resetar_senha(super().conexao_bd, usuario)
                super().conexao_bd.commit()
        return usuario_salvo