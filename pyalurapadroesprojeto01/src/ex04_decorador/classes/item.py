# -*- coding: UTF-8 -*-
# um item criado não pode ser alterado,
# suas propriedades são somente leitura
from functools import total_ordering


@total_ordering
class Item():

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f' {self.nome} : {self.valor:.2f} '

    def __eq__(self, __o):
        return self.valor == __o.valor

    def __lt__(self, __o):
        return self.valor < __o.valor
