# -*- coding: utf-8 -*-
from functools import reduce, total_ordering
import __init__
from src.ex04_decorador.classes.abstract.listaIterator\
    import ListaIterator
from src.ex04_decorador.classes.item\
    import Item

@total_ordering
class Orcamento(ListaIterator):
    def adicionar(self, *args):
        for __item in args:
            if type(__item) != Item:
                raise ValueError("Invalid!")

        return super().adicionar(*args)

    def __init__(self, *args):
        super().__init__()
        self.adicionar(*args)

    def obter_itens(self):
        return self.lista

    @property
    def total_itens(self):
        return self.tamanho

    # quando a propriedade for acessada,
    # ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        valor_total = 0
        for x1 in self.lista:
            valor_total += x1.valor
        return valor_total

    def __str__(self):
        return str(self.valor) + " >> " + super().__str__()

    def __eq__(self, __o):
        return self.valor == __o.valor

    def __lt__(self, __o):
        return self.valor < __o.valor


if __name__ == '__main__':
    e1 = Orcamento(Item('e1.1', 100), Item('e1.2', 10.1), Item('e1.3', 1210.122))
    e2 = Orcamento()
    e2.adicionar(Item('e2.1', 11), Item('e2.2', 12.1))
    e3 = Orcamento(Item('e3', 1))
    l1 = [e1, e2, e3]

    for x in sorted(l1, reverse=True):
        print(x)

    print(e1[0], e1 >= e2)
