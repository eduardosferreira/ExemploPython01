# -*- coding: utf-8 -*-
import sys
import __init__
from src.util.comum import log,\
            fnc_decoradora_tempo_processamento,\
            fnc_carrega_variavel_global,\
            fg


@fnc_decoradora_tempo_processamento
def main(*args, **kwargs):
    fnc_carrega_variavel_global(*args, **kwargs)
    log(fg.gv_ob_dict)

# Processa os dados quando acionado
if __name__ == '__main__':
    main(sys.argv, tipo_acionamento="direto")
