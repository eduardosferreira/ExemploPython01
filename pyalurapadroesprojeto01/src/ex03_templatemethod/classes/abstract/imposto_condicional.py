# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class ImpostoCondicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)

    @abstractmethod
    def deve_usar_maxima_taxacao(self, orcamento): 
        pass

    @abstractmethod
    def maxima_taxacao(self, orcamento): 
        pass

    @abstractmethod
    def minima_taxacao(self, orcamento): 
        pass
