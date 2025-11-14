from cx_Freeze import setup, Executable

base = None    

executables = [Executable("mac_api_run.py", base=base)]

packages = ["mac_api", "json","sys", "waitress"]


options = {
    'build_exe': {    
        'packages':packages,
    },    
}
print('Iniciando o SETUP....')
setup(
    name = "MAC - API",
    options = options,
    version = "1.0",
    description = 'MAC - API',
    executables = executables
)
print("\n*************** FIM ***************")