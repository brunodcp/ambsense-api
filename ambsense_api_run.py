import ambsense_api
import json
import sys
import waitress

if __name__ == "__main__":
    
    PORT = sys.argv[1] if len(sys.argv) > 1 else ambsense_api.mac_api_uteis.app_config['porta']
    if ambsense_api.mac_api_uteis.app_config['max_threads']:
        MAX_THREADS = ambsense_api.mac_api_uteis.app_config['max_threads']
    else:
        MAX_THREADS = 10
    print()
    print("########################################")
    print("# AMBSENSE API carregada com sucesso!  #")
    print("# Rodando na porta " + PORT + "...             #")
    print("# Max threads: " + MAX_THREADS + "                     #")
    print("########################################")
    
    ambsense_api.mac_api_uteis.app_logger.info("########################################")
    ambsense_api.mac_api_uteis.app_logger.info("# AMBSENSE API carregada com sucesso!  #")
    ambsense_api.mac_api_uteis.app_logger.info("# Rodando na porta " + PORT + "...             #")
    ambsense_api.mac_api_uteis.app_logger.info("# Max threads: " + MAX_THREADS + "                     #")
    ambsense_api.mac_api_uteis.app_logger.info("########################################")
    
    waitress.serve(ambsense_api.app, port=PORT, threads=MAX_THREADS)

        