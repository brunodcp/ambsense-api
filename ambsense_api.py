from flask import Flask, request, flash, abort, jsonify
from flask_cors import CORS, cross_origin

import os

import json
import copy 
from typing import List

import time
from time import mktime
from datetime import datetime, timedelta



import mac_api_uteis

from controller.perfil_controller import Perfil_controller
from controller.usuario_controller import Usuario_controller

from controller.google_api_controller import Google_api_controller

from model.funcao_model import Funcao
from model.perfil_model import Perfil
from model.usuario_model import Usuario

from uteis.conexao_mysql import Conexao_mysql
from uteis.app_config import App_config

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status_code'] = self.status_code
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(e):
    return jsonify(e.to_dict()), e.status_code



########################### ROOT ########################### 
@app.route('/')
@cross_origin()
def show_all():
    return "API AMBSENSE"

########################### Google APIs ########################### 

@app.route('/google_api/get_access_token', methods=['GET','POST'])
@cross_origin()
def google_api_get_access_token():
    access_token_info = ""

    google_api_controller = Google_api_controller()
    access_token_info = google_api_controller.get_access_token()
    
    access_token_info = '{"access_token":"' + access_token_info.access_token + '","expires_in":' + str(access_token_info.expires_in) + '}'
    
    return access_token_info

########################### Pedido ########################### 

@app.route('/teste', methods=['GET','POST'])
@cross_origin()
def teste():
    resultado = ""
    
    """
    perfil_controller = Perfil_controller()
    perfis : List[Perfil] = perfil_controller.listar_perfis()
    for perfil in perfis:
        resultado += '- ' + perfil.nome + '<br>'
        funcoes : List[Funcao] = perfil_controller.listar_funcoes(perfil)
        for funcao in funcoes:
            resultado += ' &nbsp; &nbsp; &nbsp; &nbsp; -> ' + funcao.nome + '<br>'
    """
    usuario = Usuario()
    
    try:
        usuario_controller = Usuario_controller()
        
        #usuario = usuario_controller.autenticar(usuario)

        usuario.codigo = '1'
        usuarios = usuario_controller.listar(usuario)
        if len(usuarios) > 0:
            usuario = usuarios[0]
            if (usuario != None):
                resultado = usuario.to_json()
            else:
                resultado = ""
            
            #usuario = usuario_controller.excluir(usuario)
        else:
            raise InvalidAPIUsage("Usuário não encontrado", status_code=400)
    except Exception as ex:
        print(ex.args)
        raise InvalidAPIUsage(ex.args[1], status_code=ex.args[0])
    return resultado

############################################################################

@app.route('/new', methods=['GET','POST'])
def new():
  time.sleep(1)
  if request.method == 'POST':
    if not request.form['name1'] or not request.form['id1']:
        flash ('Please enter all fields')
    else:
        return "oi"
  return "oi"

@app.after_request
def after_request(response):
    timestamp = datetime.now().strftime('[%Y-%b-%d %H:%M:%S.%f')[:-3] + ']'
    if response.status == "200 OK" or response.status == "204 OK":
        mac_api_uteis.app_logger.debug('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
        if app_config.pegar_valor('nivel_log') != "DEBUG":
            print(timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    else:
        mac_api_uteis.app_logger.error('%s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    #print(timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)
    
    return response

lst_aplicacoes = []

app_config = App_config(os.path.join("config","config.json"))
app_config.carregar_config()

if __name__ == '__main__':
    
    app.debug = (str(app_config.pegar_valor('nivel_log')) == "DEBUG")
    app.run(host = '0.0.0.0', port = app_config.pegar_valor('porta'), threaded=True)

    
