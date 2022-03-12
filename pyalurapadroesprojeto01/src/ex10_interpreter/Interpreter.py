# -*- coding: utf-8 -*-
"""

[11:34] E o padrão de projeto que utilizamos aqui para interpretar, 
para processar essa DSL é o design pattern interpreter, que é o intérprete, 
que ele vai ler isso aqui, essas nossas expressões e essa nossa DSL e, 
no final, vai interpretar isso dando um resultado, fechado? 

O padrão é bastante útil quando temos que implementar interpretadores para DSLs, 
ou coisas similares. É um padrão bem complicado, mas bastante interessante.

O padrão Interpreter é geralmente útil para interpretar DSLs (se você não sabe o que é uma DSL, pode ler mais sobre isso aqui: http://pt.wikipedia.org/wiki/Linguagem_de_dom%C3%ADnio_espec%C3%ADfico. É comum que, ao ler a string (como por exemplo 2+3/4), o programa transforme-o em uma melhor estrutura de dados (como as nossas classes Expressao) e aí interprete essa árvore.

É realmente um padrão de projeto bem peculiar, e com utilização bem específica.

"""


class Substracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia()
                - self.__expressao_direita.avalia())


class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return (self.__expressao_esquerda.avalia()
                + self.__expressao_direita.avalia())


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def avalia(self):
        return self.__numero


if __name__ == '__main__':

    expressao_esquerda = Substracao(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    resultado = expressao_conta.avalia()
    print (resultado)
