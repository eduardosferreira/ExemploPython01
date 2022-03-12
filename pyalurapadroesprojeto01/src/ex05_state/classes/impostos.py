# -*- coding: utf-8 -*-
import __init__
from src.ex05_state.classes.abstract.imposto_condicional\
    import ImpostoCondicional
from src.ex05_state.classes.abstract.imposto\
    import Imposto
from src.ex05_state.decorators.decorator\
    import IPVX


class ICMS(Imposto):
    def calcula(self, orcamento):
        return (orcamento.valor * 0.1) + self.calculo_do_outro_imposto(orcamento)


class ISS(Imposto):
    @IPVX
    def calcula(self, orcamento):
        return (orcamento.valor * 0.06) + self.calculo_do_outro_imposto(orcamento)

# código anterior omitido


class ICPP(ImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return (orcamento.valor > 500)

    def maxima_taxacao(self, orcamento):
        return (orcamento.valor * 0.07)

    def minima_taxacao(self, orcamento):
        return (orcamento.valor * 0.05)


class IKCV(ImpostoCondicional):

    def deve_usar_maxima_taxacao(self, orcamento):
        return (orcamento.valor > 500)\
            and self.__tem_item_maior_que_100_reais(orcamento)

    def maxima_taxacao(self, orcamento):
        return (orcamento.valor * 0.10)

    def minima_taxacao(self, orcamento):
        return (orcamento.valor * 0.06)

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
