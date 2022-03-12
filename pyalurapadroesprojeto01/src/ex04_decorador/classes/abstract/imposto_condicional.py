# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from src.ex04_decorador.classes.abstract.imposto import Imposto


class ImpostoCondicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento) \
                + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.minima_taxacao(orcamento) \
                + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento):
        return False

    @abstractmethod
    def maxima_taxacao(self, orcamento):
        return 0

    @abstractmethod
    def minima_taxacao(self, orcamento):
        return 0
