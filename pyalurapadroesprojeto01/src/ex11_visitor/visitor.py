# -*- coding: utf-8 -*-
"""
Quantos visitors desejarmos
Podemos criar quantos visitors desejarmos, 
até mesmo um que exiba a expressão por extenso, por exemplo. 
Porém, para que o novo visitor funcione, ele precisa ter os 
métodos visita_soma, visita_subtracao e visita_numero. 
Sabemos que pela natureza dinâmica da linguagem Python e do Duck Typing, 
o método aceita da expressões pode aceitar qualquer 
objeto que tenham esses métodos. 
Porém, nada nos impede de criarmos uma classe abstrata que contenha 
esses métodos como abstratos, obrigando a todos que herdarem 
a classe a implementarem esses métodos. 
Aliás, usamos bastante classes abstratas no primeiro treinamento de Design Patterns.


"""
from abc import ABC, abstractmethod


class Operacao(ABC):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.expressao_esquerda = expressao_esquerda
        self.expressao_direita = expressao_direita

    def _operacao(self, operacao):
        return eval("self.expressao_esquerda.avalia()"
                    + str(operacao) +
                    "self.expressao_direita.avalia()")

    @abstractmethod
    def avalia(self):
        pass

    @abstractmethod
    def aceita(self, visitor):
        pass

    def _operacao_tipo(self, operacao, tipo):
        return eval("self.expressao_esquerda.avalia()"
                    + tipo +
                    "self.expressao_direita.avalia()")

    def _avalia(self, tipo):
        return self._operacao(tipo)

    def _aceita(self, visitor, tipo):
        visitor._visita(self, tipo)


class Operadores(Operacao):

    def avalia(self, tipo):
        return self._avalia(tipo)

    def aceita(self, visitor, tipo):
        self._aceita(visitor, tipo)


class Substracao(Operacao):

    def avalia(self):
        return self._operacao("-")

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Soma(Operacao):

    def avalia(self):
        return self._operacao("+")

    def aceita(self, visitor):
        visitor.visita_soma(self)


class Multiplicacao(Operacao):

    def avalia(self):
        return self._operacao("*")

    def aceita(self, visitor):
        visitor.visita_multiplicacao(self)


class Divisao(Operacao):

    def avalia(self):
        return self._operacao("/")

    def aceita(self, visitor):
        visitor.visita_divisao(self)


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)


class Impressora(object):

    def _decorator_imprimir(metodo_ou_funcao):
        def wrapper(self, operacao):
            print('(', end='')
            operacao.expressao_esquerda.aceita(self)
            metodo_ou_funcao(self, operacao)
            operacao.expressao_direita.aceita(self)
            print(')', end='')
        return wrapper

    def _visita(self, operacao, tipo=None):
        print('(', end='')
        operacao.expressao_esquerda.aceita(self, tipo)
        print(tipo, end='')
        operacao.expressao_direita.aceita(self, tipo)
        print(')', end='')

    @_decorator_imprimir
    def visita_soma(self, operacao):
        print('+', end='')

    @_decorator_imprimir
    def visita_subtracao(self, operacao):
        print('-', end='')

    @_decorator_imprimir
    def visita_multiplicacao(self, operacao):
        print('-', end='')

    @_decorator_imprimir
    def visita_divisao(self, operacao):
        print('/', end='')

    def visita_numero(self, numero):
        print(numero.avalia(), end='')


class Prefixa_Visitor(Impressora):

    def _decorator_imprimir(metodo_ou_funcao):
        def wrapper(self, operacao):
            metodo_ou_funcao(self, operacao)
            print('(', end='')
            operacao.expressao_esquerda.aceita(self)
            print('<->', end='')
            operacao.expressao_direita.aceita(self)
            print(')', end='')
        return wrapper

    def _visita(self, operacao, tipo=None):
        print('(', end='')
        operacao.expressao_esquerda.aceita(self, tipo)
        print(tipo, end='')
        operacao.expressao_direita.aceita(self, tipo)
        print(')', end='')

    @_decorator_imprimir
    def visita_soma(self, operacao):
        print('+', end='')

    @_decorator_imprimir
    def visita_subtracao(self, operacao):
        print('-', end='')

    @_decorator_imprimir
    def visita_multiplicacao(self, operacao):
        print('-', end='')

    @_decorator_imprimir
    def visita_divisao(self, operacao):
        print('/', end='')

    def visita_numero(self, numero):
        print(numero.avalia(), end='')


if __name__ == '__main__':

    print()
    print('INICIO', '*'*20)
    expressao_esquerda = Substracao(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)
    resultado = expressao_conta.avalia()
    visitor = Impressora()
    print('expressao...: ', end='')
    expressao_conta.aceita(visitor)
    print(' : ', resultado)
    print('FIM   ', '*'*20)
    print()
