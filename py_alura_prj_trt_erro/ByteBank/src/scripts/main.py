# -*- coding: utf-8 -*-
from datetime import datetime
import sys
import os
from typing import List
import __init__
from src.util.comum import (log,
                            fnc_decoradora_tempo_processamento,
                            main as comum_main,
                            fnc_encoding_arquivo,
                            fg)


@fnc_decoradora_tempo_processamento
def main():
    comum_main(sys.argv, tipo_acionamento="direto")
    path_diretorio: str = os.path.abspath(
        os.path.join(os.path.dirname(__file__),
                     "..", "dados"))
    if os.path.isdir(path_diretorio):
        lista_arquivo: List(str) = [
            x for x in os.listdir(path_diretorio)
            if len(os.path.splitext(x)) > 1
            and str(os.path.splitext(x)[1]).upper().strip() == '.CSV'
        ]
        for arquivo in lista_arquivo:
            path_arquivo_leitura: str = os.path.join(path_diretorio, arquivo)
            path_arquivo_escrita: str = os.path.join(path_diretorio,
                                                     os.path.splitext(
                                                         arquivo)[0]
                                                     + datetime.now().strftime(
                                                         "%Y%m%d_%H%M%S")
                                                     + '.log')
            path_arquivo_escrita_csv: str = os.path.join(path_diretorio,
                                                         os.path.splitext(
                                                             arquivo)[0]
                                                         + '_2.csv')
            log(path_arquivo_leitura, path_arquivo_escrita)
            try:
                # https://stackoverflow.com/questions/9282967/how-to-open-a-file-using-the-open-with-statement
                arq_escrita_csv = open(file=path_arquivo_escrita_csv,
                                       mode='a',
                                       encoding=fnc_encoding_arquivo(
                                           path_arquivo_escrita_csv, 'a')
                                       )
                with open(file=path_arquivo_escrita,
                          mode='w',
                          encoding=fnc_encoding_arquivo(
                              path_arquivo_escrita, 'w')
                          ) as arq_escrita, open(
                        file=path_arquivo_leitura,
                        mode='r',
                        encoding=fnc_encoding_arquivo(path_arquivo_leitura)
                ) as arq_leitura:
                    for linha in arq_leitura:
                        arq_escrita.write(linha.strip().split(",")[-1]+"\n")
                        arq_escrita.flush()
                        # try:
                        #     teclado = eval(input(""))
                        #     teclado
                        # except Exception:
                        #     pass
                        arq_escrita_csv.write(path_arquivo_escrita
                                              + ","
                                              + linha)
            except IsADirectoryError as ds_err:
                log(" >> Problemas no diretório >> " + str(ds_err))
            except PermissionError as ds_err:
                log(" >> Sem permissao na leitura do arquivo >> "
                    + str(ds_err))
            except FileNotFoundError as ds_err:
                log(" >> Problemas ao encontrar arquivo >> " + str(ds_err))
            except Exception as ds_err:
                log(" >> Problemas desconhecido >> " + str(ds_err))
            finally:
                try:
                    arq_escrita_csv.close()
                except Exception:
                    pass
            try:
                arq_leitura = open(
                    file=path_arquivo_escrita,
                    mode='r',
                    encoding=fnc_encoding_arquivo(path_arquivo_escrita)
                )
                while True:
                    linha = arq_leitura.readline()
                    if not linha:
                        break
                    log(linha.strip())
            # If destination is a directory.
            except IsADirectoryError as ds_err:
                log(" >> Problemas no diretório >> " + str(ds_err))
            except PermissionError as ds_err:
                log(" >> Sem permissao na leitura do arquivo >> "
                    + str(ds_err))
            except FileNotFoundError as ds_err:
                log(" >> Problemas ao encontrar arquivo >> " + str(ds_err))
            except Exception as ds_err:
                log(" >> Problemas desconhecido >> " + str(ds_err))
            finally:
                try:
                    arq_leitura.close()
                except Exception:
                    pass


# Processa os dados quando acionado
if __name__ == '__main__':
    main()
