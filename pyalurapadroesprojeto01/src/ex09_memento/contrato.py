# -*- coding: utf-8 -*-
# contrato.py
from datetime import date


class Estado(object):
    """
Para que serve a classe Estado? 
Não poderíamos simplesmente guardar a classe Contrato de uma vez na lista?

RESPONDA
Opinião do instrutor

Sim, poderíamos guardar diretamente a lista de Contratos. 
Mas veja que isso depende do problema. 
No nosso caso, não tínhamos outra informação para associar ao "estado". 
Se tivéssemos que armazenar, por exemplo, a data que o estado foi salvo, 
a classe Estado faria sentido.

As definições de padrões de projeto 
são geralmente as mais genéricas possíveis para dar suporte a qualquer problema. 
Mas você obviamente deve implementar o padrão de acordo com o seu problema.

Problemas do memento
PRÓXIMA ATIVIDADE

Você consegue ver algum possível problema do padrão Memento? Se sim, qual?

RESPONDA
Opinião do instrutor

Um possível problema é a quantidade de memória que ele pode ocupar, 
afinal estamos guardando muitas instâncias de objetos que podem ser pesados.

Por isso, dependendo do tamanho dos seus objetos, 
a classe Estado pode passar a guardar não o objeto todo, 
mas sim somente as propriedades que mais fazem sentido.

Nada impede você também de limitar a quantidade máxima de objetos no histórico 
que será armazenado.

    """
    def __init__(self, contrato):
        self.__contrato = contrato

    @property
    def contrato(self):
        return self.__contrato


class Historico(object):

    def __init__(self):
        self.__estados_salvos = []

    def obtem_estado(self, indice):
        return self.__estados_salvos[indice]

    def adiciona_estado(self, estado):
        self.__estados_salvos.append(estado)


class Contrato(object):

    def __init__(self, data, cliente, tipo="NOVO"):
        self.__data = data
        self.__cliente = cliente
        self.__tipo = tipo

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    def avanca(self):
        if self.__tipo == 'NOVO':
            self.__tipo = 'EM ANDAMENTO'
        elif self.__tipo == 'EM ANDAMENTO':
            self.__tipo = 'ACERTADO'
        elif self.__tipo == 'ACERTADO':
            self.__tipo = 'CONCLUIDO'

    def salva_estado(self):
        return Estado(Contrato(data=self.__data,
                               cliente=self.__cliente,
                               tipo=self.__tipo))

    def restaura_estado(self, estado):
        self.__data = estado.contrato.data
        self.__cliente = estado.contrato.cliente
        self.__tipo = estado.contrato.tipo


if __name__ == '__main__':

    historico = Historico()

    contrato = Contrato(data=date.today(),
                        cliente='Flávio Almeida')

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.avanca()
    historico.adiciona_estado(contrato.salva_estado())

    contrato.restaura_estado(historico.obtem_estado(1))
    print('Tipo do contrato restaurado %s' % (contrato.tipo))
