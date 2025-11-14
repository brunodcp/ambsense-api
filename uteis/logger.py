import logging
from logging.handlers import TimedRotatingFileHandler

_logger = None

def carregar_log(nome, nivel_log):
    global _logger
    try:
        strArqLog = "./log/" + nome + "_api.log"
        log_level = None
        if   nivel_log.upper() == "DEBUG":      log_level=logging.DEBUG
        elif nivel_log.upper() == "INFO":       log_level=logging.INFO
        elif nivel_log.upper() == "WARNING":    log_level=logging.WARNING
        elif nivel_log.upper() == "ERROR":      log_level=logging.ERROR
        elif nivel_log.upper() == "CRITICAL":   log_level=logging.CRITICAL
        elif nivel_log.upper() == "FATAL":      log_level=logging.FATAL
        else:                                   log_level=logging.NOTSET
        
        _logger = logging.getLogger("mac_api")
        _logger.setLevel(log_level)
        if not _logger.hasHandlers():
            # add a rotating handler
            handler = TimedRotatingFileHandler(strArqLog,
                                            when="d",
                                            interval=1,
                                            backupCount=10,
                                            encoding="utf-8")
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(
                format,
                datefmt='%d/%m/%Y %H:%M:%S')
            #formatter.converter = datetime.now().timetuple() # if you want UTC time
            handler.setFormatter(formatter)
            _logger.addHandler(handler)

        return True
    except Exception as ex:
        return False