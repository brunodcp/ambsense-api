import mysql.connector

from typing import List

class Conexao_mysql:

    def __init__(self, host : str, porta : str, usuario:str, senha:str, banco:str):
        self.host : str = host
        self.porta : str = porta
        self.usuario : str = usuario
        self.senha : str = senha
        self.banco : str = banco
        self._conexao = None

    def __del__(self):
        self.fechar()
        self.host = None
        self.porta = None
        self.usuario = None
        self.senha = None
        self.banco = None
        self._conexao = None

    def conectar(self) -> bool:
        try:
            self._conexao = mysql.connector.connect(user=self.usuario, password=self.senha,
                                                host=self.host, port=self.porta,
                                                database=self.banco)
            return True
        except Exception as ex:
            print(str(ex.args))
            self._conexao = None
            return False

    def consultar_sql(self, consulta: str) -> List[any] | None:
        lst_resultado = None
        
        try:
            cursor = self._conexao.cursor()
            cursor.execute(consulta)
            lst_resultado = cursor.fetchall()
            cursor.close()
        except Exception as ex:
            print("ERRO - " + str(ex.args))
        
        return lst_resultado
    
    def cursor(self):
        if self._conexao != None:
            return self._conexao.cursor()
        else:
            return None
            

    def commit(self):
        if self._conexao != None:
            self._conexao.commit()
            
    
    def fechar(self):
        if self._conexao != None:
            self._conexao.close()
            self._conexao = None

