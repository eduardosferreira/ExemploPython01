#!/usr/local/bin/python3.7
# -*- coding: utf-8 -*-
"""
----------------------------------------------------------------------------------------------
  MODULO ...: TESHUVA
  SCRIPT ...: loaderGenerico.py
  CRIACAO ..: 24/06/2021
  AUTOR ....: EDUARDO DA SILVA FERREIRA / KYROS TECNOLOGIA
  DESCRICAO : Atraves de um arquivo de layout monta um ctl que faz a carga na tabela
                gfcadastro.BILLING_COMBINADO do arquivo citado no ambiente informado.

----------------------------------------------------------------------------------------------
  HISTORICO :


----------------------------------------------------------------------------------------------
"""

import datetime
import os
import sys
import shutil
import traceback

nome_script = os.path.basename( sys.argv[0] ).replace('.py', '')

import comum
import sql
variaveis = {'teste': '001'}
comum.variaveis = variaveis
sql.variaveis = variaveis
from layout import *


log.gerar_log_em_arquivo = True


