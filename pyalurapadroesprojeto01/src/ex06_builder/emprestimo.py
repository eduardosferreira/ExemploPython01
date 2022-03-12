# -*- coding: UTF-8 -*-
class Emprestimo(object):

    def __init__(self, parcelas, valor, data_de_vencimento, bonus=0):
        self.parcelas = parcelas
        self.valor = valor
        self.bonus = bonus
        self.data_de_vencimento = data_de_vencimento
