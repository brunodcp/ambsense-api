from typing import List

from dao.dispositivo_dao import Dispositivo_dao
from model.dispositivo_model import Dispositivo

class Dispositivo_controller:
    def __init__(self):
        super().__init__()

    def listar(dispositivo : Dispositivo) -> List[Dispositivo] :
        dispositivo_dao = Dispositivo_dao()
        dispositivos : List[Dispositivo] = []
        if super().conexao_bd.conectar():    
            dispositivos = dispositivo_dao.listar(super().conexao_bd, dispositivo)
             
            super().conexao_bd.fechar()
        
        return dispositivos
    
    def salvar (self, dispositivo :Dispositivo) -> Dispositivo:
        dispositivo_dao = Dispositivo_dao()
        dispositivo_salvo: Dispositivo = None
        if (dispositivo.nome == None or dispositivo.nome == ""):
            raise Exception(400, "O Nome do dispositivo não foi informado")
        elif (dispositivo.serial == None or dispositivo.serial == "") :
            raise Exception(400, "O serial do dispositivo não foi informado")
        else:
            if super().conexao_bd.conectar():    
                dispositivo_salvo = dispositivo_dao.salvar(super().conexao_bd, dispositivo)
                super().conexao_bd.commit()
        return dispositivo_salvo
    
    def excluir (self, dispositivo :Dispositivo) -> Dispositivo:
        dispositivo_dao = Dispositivo_dao()
        dispositivo_salvo: Dispositivo = None
        if (dispositivo.codigo == None or dispositivo.codigo == ""):
            raise Exception(400, "Dispositivo não identificado")
        else:
            if super().conexao_bd.conectar():    
                dispositivo_salvo = dispositivo_dao.excluir(super().conexao_bd, dispositivo)
                super().conexao_bd.commit()
        return dispositivo_salvo