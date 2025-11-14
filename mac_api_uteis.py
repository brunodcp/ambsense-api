from urllib3 import ProxyManager, make_headers, PoolManager
import ssl

import os

from pathlib import Path

from datetime import datetime, timedelta

import json

import hashlib

import logging
from logging.handlers import TimedRotatingFileHandler

def carregar_config():
    global app_config
    try:
        strArqConf = os.path.join("config","config.json")
        with open(strArqConf, mode='r', encoding="utf-8") as json_agente:
            app_config = json.load(json_agente)
        return True
    except Exception as ex:
        print("Falhou ao carregar o arquivo de configuração \r\n" + str(ex.args) ) 
        return False

def carregar_log(nivel_log):
    
    strArqLog = os.path.join("log","mac_api.log")
    log_level = None
    if   nivel_log.upper() == "DEBUG":      log_level=logging.DEBUG
    elif nivel_log.upper() == "INFO":       log_level=logging.INFO
    elif nivel_log.upper() == "WARNING":    log_level=logging.WARNING
    elif nivel_log.upper() == "ERROR":      log_level=logging.ERROR
    elif nivel_log.upper() == "CRITICAL":   log_level=logging.CRITICAL
    elif nivel_log.upper() == "FATAL":      log_level=logging.FATAL
    else:                                   log_level=logging.NOTSET
    
    logger = logging.getLogger("mac_api")
    logger.setLevel(log_level)
    if not logger.hasHandlers():
        # add a rotating handler
        handler = TimedRotatingFileHandler(strArqLog,
                                        when="d",
                                        interval=1,
                                        backupCount=1,
                                        encoding="utf-8")
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(
            format,
            datefmt='%d/%m/%Y %H:%M:%S')
        #formatter.converter = datetime.now().timetuple() # if you want UTC time
        #handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def pegar_http_client() :
    proxy_host = ''
    proxy_host = str(app_config['proxy'])
    ctx = ssl.create_default_context()
    ctx.set_ciphers('DEFAULT@SECLEVEL=1')
    
    #Configura o proxy
    if (proxy_host != ""):
        protocolo = proxy_host.split('://')[0]
        proxy_host = proxy_host.replace(protocolo + '://', '')
        auth_str = proxy_host.split('@')[0]
        proxy_host = proxy_host.split('@')[1]
        default_headers = make_headers(proxy_basic_auth=auth_str)
        http = ProxyManager(protocolo + "://" + proxy_host + "/", proxy_headers=default_headers,
   ssl_version=ssl.PROTOCOL_TLS,
   ssl_context=ctx)       
        
    else: #Sem proxy
        http = PoolManager(
            ssl_version=ssl.PROTOCOL_TLS,
            ssl_context=ctx)
    return http


def validar_guest_auth_token(guest_token) :

    arq_path = app_config["path_dados"] + '\\api_guests\\tokens.json'
    guest = None

    #print("validando o token : ", guest_token)
    lst_tokens = []
    if os.path.exists(arq_path) :
        with open(arq_path, "r") as arq_tokens:
            lst_tokens = json.load(arq_tokens)
    
    for token in lst_tokens:
        if token['token'] == guest_token:
            guest = token['guest']
    
    return guest

def validar_auth_token(token) :
    #print("validando o token : ", token)
    TOKEN_KEY = "nova_fibra_token"
    lst_chave = []
    data_agora = datetime.utcnow()
    data_agora -= timedelta(seconds=5)
    for i in range(10):
        data_agora += timedelta(seconds=1)
        chave = (TOKEN_KEY + 
                 ("0" + str(data_agora.hour))[-2:] + 
                 ("0" + str(data_agora.minute))[-2:] + 
                 ("0" + str(data_agora.second))[-2:] ).encode('utf-8')
        #print(chave)
        chave = hashlib.md5(chave).hexdigest()
        #print(data_agora,  chave)
        lst_chave.append(chave)
    #print(token)
    if token in lst_chave :
        #print("TOKEN OK")
        return True
    else:
        #print("TOKEN NOK")
        return False



##########################################################
app_config = None
app_logger = None

user_tratconv = "OI310203"
pass_tratconv = "N0v@f1br@1a2#"


if carregar_config():
    app_logger = carregar_log(app_config['nivel_log'])