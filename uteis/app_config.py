import json

class App_config:
    def __init__(self, path=None) -> None:
        self._app_config = None
        self.path = path

    def carregar_config(self, path=None):
        try:
            if path == None: path = self.path
            
            with open(path, mode='r', encoding="utf-8") as json_agente:
                self._app_config = json.load(json_agente)
            return True
        except Exception as ex:
            print("Falhou ao carregar o arquivo de configuração \r\n" + str(ex.args) ) 
            return False
        
    def pegar_valor(self, propriedade):
        return self._app_config[propriedade]