# -*- coding: utf-8 -*-
import sys
import __init__
from src.util.comum import log
from src.scripts.teste01.teste01 import main as main_teste01

# Processa os dados quando acionado
if __name__ == '__main__':
    log('Teste')
    #main_teste01(sys.argv, tipo_acionamento="direto")
    import os
    # c = r'c:\Users\Kyros\VSProjects\UdemyPhyton3LuizOtavio\prj_PyQT5\src\scripts'
    # c = r'c:\Users\Kyros\Temp01\02'
    # print(os.path.dirname(c))
    print(sys.path)
    

