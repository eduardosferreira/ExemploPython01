# -*- coding: utf-8 -*-
"""
O mais importante aqui é pensar na manutenção do seu código, tendo em vista a certeza de que seu código vai mudar. A solução procedural é fácil de se implementar, mas difícil de manter. Já, a consideração da aplicação de um padrão de projeto pode ser demorada, 
mas surte efeitos na manutenção e legibilidade do seu código.

A principal situação que faz emergir o Design Pattern State
 é a necessidade de implementação de uma máquina de estados. Geralmente, o controle das possíveis transições entre estados são várias, também são complexas, fazendo com que a implementação não seja simples. O State auxilia a manter o controle dos estados simples e organizados, através da criação de classes que representem cada estado e sabendo controlar as transições entre eles.

"""
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.ex05_state.classes.orcamento import Orcamento
from src.ex05_state.classes.item import Item
from src.ex05_state.classes.factory.calculador_de_descontos\
    import Calculador_de_descontos
from src.ex05_state.classes.factory.calculador_de_impostos\
    import Calculador_de_impostos
from src.ex05_state.classes.impostos\
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
