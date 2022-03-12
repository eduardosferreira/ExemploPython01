# -*- coding: utf-8 -*-
import sys
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.scripts.teste01.teste01 import main as main_teste01
from src.classes.retangulo import Retangulo


@fnc_decoradora_tempo_processamento
def main(*args, **kwargs):
    r = Retangulo(7, 6)
    r.area = 7
    log(r.area)
    log(r.obter_area())
    

# Processa os dados quando acionado
if __name__ == '__main__':
    main_teste01(sys.argv, tipo_acionamento="direto")
    log(sys.path)    
    main(sys.argv[0])
    #import os
    # c = r'c:\Users\Kyros\VSProjects\UdemyPhyton3LuizOtavio\prj_PyQT5\src\scripts'
    #c = r'c:\Users\Kyros\Temp01\02'
    # print(os.path.dirname(c))
