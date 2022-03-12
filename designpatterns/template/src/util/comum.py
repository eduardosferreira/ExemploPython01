# -*- coding: utf-8 -*-

# Imports
import os
from datetime import datetime
from time import time

# Funcoes


def fg():
    pass


def fnc_formata_data_hora(p_dt_dado: datetime = datetime.now(),
                          p_cc_formato: str = '%d/%m/%Y %H:%M:%S') -> str:
    return str(p_dt_dado.strftime(p_cc_formato))


def fnc_transforma_data_hora(p_cc_data: str = fnc_formata_data_hora(),
                             p_cc_formato: str = '%d/%m/%Y %H:%M:%S') -> datetime:
    return datetime.strptime(p_cc_data, p_cc_formato)


def df():
    return fnc_formata_data_hora()


def imprime_com_destaque(funcao):
    def wrapper(*args, **kwargs):
        return "\n" + str('*'*60) + "\n" + funcao(*args, **kwargs)\
            + "\n" + str('*'*60) + "\n"
    return wrapper


@imprime_com_destaque
def imprime_destaque(frase):
    return frase


def log(*args):
    print(df(), ' '.join([str(x)
                          if str(x).upper().strip().find("ERRO") < 0
                          else imprime_destaque("\n**ERRO**\n\n"
                                                + str(x) + "\n\n")
                          for x in args]))


def fnc_decoradora_tempo_processamento(p_ob_funcao: object) -> object:
    def __fnc_dependente(*args, **kwargs):
        print(df(), "Inicio", p_ob_funcao.__name__, sep=' -> ')
        v_nr_start = time()
        # Executa a função
        v_ob_resultado = p_ob_funcao(*args, **kwargs)
        # Tempo final
        v_nr_end = time()
        # Resultado de tempo em ms
        v_nr_tempo = (v_nr_end - v_nr_start) * 1000
        print(df(), "Fim", p_ob_funcao.__name__,  sep=' -> ')
        # Mostra o tempo
        print(
            df(), f'\nA função {p_ob_funcao.__name__} levou {v_nr_tempo:.2f}ms para ser executada.', '\n')
        # Retorna a função original executada
        return v_ob_resultado
    # Retorna a função que __fnc_dependente
    return __fnc_dependente


@fnc_decoradora_tempo_processamento
def fnc_carrega_variavel_global(*args, **kwargs):
    """
        Funcao principal
    """
    fg.gv_ob_dict = dict()
    fg.gv_ob_dict['sep_dir'] = ('/' if os.name == 'posix' else '\\')
    fg.gv_ob_dict['file'] = __file__
    fg.gv_ob_dict['basename'] = os.path.basename(__file__)
    fg.gv_ob_dict['dirname'] = os.path.dirname(__file__)
    fg.gv_ob_dict['abspath'] = os.path.abspath(__file__)
    fg.gv_ob_dict['absdirname'] = os.path.dirname(os.path.abspath(__file__))
    fg.gv_ob_dict['entrada'] = []
    fg.gv_ob_dict['entrada_chaves'] = []
    fg.gv_ob_dict['tipo_acionamento'] = ""
    v_cc_key = ""
    for index, arg in enumerate(args):
        # print(df(), index, ") arg: ", arg)
        if isinstance(arg, (list, tuple)):
            if index == 0 and len(arg) > 1:
                fg.gv_ob_dict['entrada'] = arg[1:]
            for k, v in enumerate(arg):
                # print(df(), index, ".", k, ")", v)
                if v and v_cc_key and v_cc_key in fg.gv_ob_dict:
                    fg.gv_ob_dict[v_cc_key] = v
                v_cc_key = ""
                if v.startswith("-") and len(v) > 1:
                    v_cc_key = str(v).replace(":", "").strip().upper()
                    fg.gv_ob_dict[v_cc_key] = v
                if str(index) + "." + str(k) not in fg.gv_ob_dict:
                    fg.gv_ob_dict[str(index) + "." + str(k)] = v
        if str(index) not in fg.gv_ob_dict:
            fg.gv_ob_dict[str(index)] = arg

    for index, (key, arg) in enumerate(kwargs.items()):
        # print(df(), index, ") kwarg>> ", "[", key, "]:", arg)
        fg.gv_ob_dict[str(key)] = arg
        if isinstance(arg, (list, tuple)):
            for k, v in enumerate(arg):
                print(df(), index, ".", k, ")", v)
                if str(key)+"." + str(index) + "." + str(k) not in fg.gv_ob_dict:
                    fg.gv_ob_dict[str(key)+"." + str(index) + "." + str(k)] = v
        if str(key)+"." + str(index) not in fg.gv_ob_dict:
            fg.gv_ob_dict[str(key)+"." + str(index)] = v

    fg.gv_ob_dict['entrada_chaves'] = [{str(v).replace(":", "").strip().upper(): fg.gv_ob_dict.get(
        str(v).replace(":", "").strip().upper(), "")} for v in fg.gv_ob_dict['entrada'] if v.startswith("-")]
    # print(df(), '-entrada:', str(fg.gv_ob_dict['entrada']))
    # print(df(), '-tipo_acionamento:', str(fg.gv_ob_dict['tipo_acionamento']))
    # print(df(), '-entrada_chaves:', str(fg.gv_ob_dict['entrada_chaves']))
    # print(df(), '-dict:', str(fg.gv_ob_dict))


@fnc_decoradora_tempo_processamento
def main(*args, **kwargs):
    fnc_carrega_variavel_global(*args, **kwargs)
    # log(fg.gv_ob_dict)


fg()
