# -*- coding: utf-8 -*-
import __init__
from src.ex02_chainofresponsibility.classes.descontos\
    import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhentos_reais, Sem_desconto


class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        )

        return desconto.calcula(orcamento)
