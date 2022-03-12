# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from functools import reduce


class Imposto(object):

    __metaclass__ = ABCMeta

    def __init__(self, *outros_impostos):
        self.__outro_imposto = set()
        for __outro_imposto in outros_impostos:
            self.__outro_imposto.add(__outro_imposto)

    def calculo_do_outro_imposto(self, orcamento):
        valor_calculo = 0
        for __outro_imposto in self.__outro_imposto:
            valor_calculo +=\
                __outro_imposto.calcula(orcamento)
        return valor_calculo

    @abstractmethod
    def calcula(self, orcamento):
        return float(0)
