import sys
import os


def __fnc_load_path():
    """
        Funcao de carregamento path
    """
    v_cc_sep_dir = ('/' if os.name == 'posix' else '\\')
    v_cc_path = ""
    for index, dir in \
            enumerate(os.path.dirname(__file__).split(v_cc_sep_dir)):
        if index == 0:
            v_cc_path += dir+v_cc_sep_dir
            continue
        if dir.upper().strip() == "SRC":
            sys.path.append(v_cc_path)
            break
        v_cc_path = os.path.join(v_cc_path, dir)


# Carrega os dados principais
__fnc_load_path()
