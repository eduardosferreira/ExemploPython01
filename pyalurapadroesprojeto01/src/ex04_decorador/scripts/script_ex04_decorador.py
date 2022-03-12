# -*- coding: utf-8 -*-
"""
Sempre que percebemos que temos comportamentos que podem 
ser formados por comportamentos de outras classes envolvidas
 em uma mesma hierarquia, como foi o caso dos impostos, 
 que podem ser composto por outros impostos. 
 O Decorator introduz a flexibilidade na composição desses comportamentos, 
 bastando escolher no momento da instanciação, 
 quais instancias serão utilizadas para realizar o trabalho.

Um decorador é um padrão de design em Python que permite ao usuário adicionar novas funcionalidades a um objeto existente sem modificar sua estrutura. Decoradores geralmente são chamados antes da definição de uma função que você deseja decorar. Neste tutorial, mostraremos ao leitor como eles podem usar decoradores em suas funções Python.

Funções em Python são cidadãos de primeira classe . Isso significa que eles suportam operações como ser passado como argumento, retornado de uma função, modificado e atribuído a uma variável. Este é um conceito fundamental para entender antes de nos aprofundarmos na criação de decoradores Python.

Os padrões são muitas vezes parecidos. O que muda é a intenção e um detalhe da implementação. Aqui não é diferente. O Decorator é para compor e dividir comportamento em fatias onde cada fatia (objeto) representa uma parte da responsabilidade. Os Decorators modificam/melhoram o comportamento original. A intenção do Chain of Responsabilidade não é dividir a responsabilidade em fatias menores e sim criar uma cadeia de decisão onde cada objeto representa uma responsabilidade.

Um exemplo clássico de um Decorator é a leitura de um arquivo. Imagine uma classe que saiba abrir um arquivo para ler dados binários. Nem sempre queremos ler bits e bytes quando se trata de texto. Sendo assim, podemos criar uma classe que decora o comportamento para transformar 2 byte em um caracter, por exemplo. Ler um arquivo caracter por caracter,também não é tão funcional, melhor seria linha por linha. Podemos criar mais um decorator que transforma os caracteres em strings. Os decorators nesse exemplo melhoram o comportamento original (leitura) e dividem a responsabilidade.



Repare que cada padrão tem uma intenção, mas como você realmente o utiliza depende da sua aplicação.

"""
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.ex04_decorador.classes.orcamento import Orcamento
from src.ex04_decorador.classes.item import Item
from src.ex04_decorador.classes.factory.calculador_de_descontos\
    import Calculador_de_descontos
from src.ex04_decorador.classes.factory.calculador_de_impostos\
    import Calculador_de_impostos
from src.ex04_decorador.classes.impostos\
    import ISS, ICMS, ICPP, IKCV


@fnc_decoradora_tempo_processamento
def main():
    log("")
    log("*"*10)

    orcamento = Orcamento()
    orcamento.adicionar(Item('Item A', 250.0), Item('Item B', 50.0))
    orcamento.adicionar(Item('Item C', 200.0))
    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    for item in sorted(orcamento.listagem(), reverse=True):
        log(item)
    log(f'Desconto calculado : {desconto:.2f}')
    # imprime 38.5
    calculador_de_impostos = Calculador_de_impostos()
    log('ISS e ICMS')
    log(calculador_de_impostos.realiza_calculo(orcamento, ISS()))
    log(calculador_de_impostos.realiza_calculo(orcamento, ICMS()))
    # cálculo dos novos impostos
    log('ICPP e IKCV')
    log(calculador_de_impostos.realiza_calculo(
        orcamento, ICPP()))  # imprime 25.0
    log(calculador_de_impostos.realiza_calculo(
        orcamento, IKCV()))  # imprime 30.0
    log("*"*10)
    log('TODOS IMPOSTOS')
    log(calculador_de_impostos.realiza_calculo(
        orcamento, ICPP(IKCV(), ISS(), IKCV())))  # imprime 25.0
    log(calculador_de_impostos.realiza_calculo(
        orcamento, IKCV(ICPP())))  # imprime 30.0
    log("*"*10)
    log("")

# Processa os dados quando acionado
if __name__ == '__main__':
    main()
