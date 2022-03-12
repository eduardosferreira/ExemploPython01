# -*- coding: utf-8 -*-
import __init__
from src.ex03_templatemethod.classes.abstract.imposto_condicional\
    import ImpostoCondicional


class ICMS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ISS():
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

# código anterior omitido


class ICPP(ImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.07

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(ImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return orcamento.valor * 0.10

    def minima_taxacao(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
