# -*- coding: utf-8 -*-
from functools import total_ordering
import __init__
from src.ex05_state.classes.abstract.listaIterator\
    import ListaIterator
from src.ex05_state.classes.item\
    import Item
from src.ex05_state.classes.enumerator.statusorcamento\
    import StatusOrcamento


@total_ordering
class Orcamento(ListaIterator):
    def adicionar(self, *args):
        for __item in args:
            if type(__item) != Item:
                raise ValueError("Invalid!")

        return super().adicionar(*args)

    def __init__(self, *args):
        super().__init__()
        self.__estado_atual = StatusOrcamento.Em_Aprovacao.value[0]
        self.__desconto_extra = 0.0
        self.adicionar(*args)

    def aplica_desconto_extra(self):
        valor_desconto = StatusOrcamento.taxa_desconto(self.__estado_atual)
        if valor_desconto is None or not valor_desconto:
            raise ValueError("Orçamento não recebe desconto devido ao seu estado! " +
                             str(StatusOrcamento.descricao_valor(self.__estado_atual)))
        self.__desconto_extra += self.valor * valor_desconto

    def obter_itens(self):
        return self.lista

    @property
    def estado(self):
        return StatusOrcamento.descricao_valor(self.__estado_atual)

    def aprova(self):
        if self.__estado_atual is None\
                or StatusOrcamento.aprovar(self.__estado_atual) is None:
            raise ValueError("Orçamento não pode ser aprovado devido ao seu estado! " +
                             str(StatusOrcamento.descricao_valor(self.__estado_atual)))

        self.__estado_atual = StatusOrcamento.Aprovado.value[0]

    def reprova(self):
        if self.__estado_atual is None\
                or StatusOrcamento.aprovar(self.__estado_atual) is None:
            raise ValueError("Orçamento não pode ser aprovado devido ao seu estado! " +
                             str(StatusOrcamento.descricao_valor(self.__estado_atual)))

        self.__estado_atual = StatusOrcamento.Reprovado.value[0]

    def finaliza(self):
        if self.__estado_atual is None\
                or StatusOrcamento.aprovar(self.__estado_atual) is None:
            raise ValueError("Orçamento não pode ser aprovado devido ao seu estado! " +
                             str(StatusOrcamento.descricao_valor(self.__estado_atual)))

        self.__estado_atual = StatusOrcamento.Finalizado.value[0]

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
        return "Estado: " + str(self.estado) +\
            " >> Total: " + str(self.valor) +\
            " >> Desconto: " + str(self.__desconto_extra) +\
            " >> \n" + super().__str__()

    def __eq__(self, __o):
        return self.valor == __o.valor

    def __lt__(self, __o):
        return self.valor < __o.valor


if __name__ == '__main__':
    e1 = Orcamento(Item('e1.1', 100), Item(
        'e1.2', 10.1), Item('e1.3', 1210.122))
    e2 = Orcamento()
    e2.adicionar(Item('e2.1', 11), Item('e2.2', 12.1))
    e3 = Orcamento(Item('e3', 1))
    e3.aplica_desconto_extra()
    e3.aprova()
    e3.aprova()
    l1 = [e1, e2, e3]

    for x in sorted(l1, reverse=True):
        print(x)

    print(e1[0], e1 >= e2)
