# -*- coding: utf-8 -*-
import sys
import __init__
from src.util.comum import log,\
    fnc_decoradora_tempo_processamento,\
    main as comum_main,\
    fg        


@fnc_decoradora_tempo_processamento
def main():
    comum_main(sys.argv, tipo_acionamento="direto")
    log(fg.gv_ob_dict)


# Processa os dados quando acionado
if __name__ == '__main__':
    main()


