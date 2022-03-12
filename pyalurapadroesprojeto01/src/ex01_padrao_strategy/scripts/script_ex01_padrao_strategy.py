# -*- coding: utf-8 -*-
"""
Um padrão de projeto é uma solução elegante para um problema que é recorrente no dia-a-dia do desenvolvedor.

Por mais que desenvolvamos projetos diferentes, muitos dos problemas se repetem. Padrões de projeto são soluções elegantes e flexíveis para esses problemas.

Por mais que desenvolvamos projetos diferentes, muitos dos problemas se repetem. Padrões de projeto são soluções elegantes e flexíveis para esses problemas.
Sobre a motivação dos padrões de projeto, temos as seguintes afirmativas:

1) O mais importante ao estudar padrões de projeto é entender qual a real motivação do padrão, e quando ele deve ser aplicado.

2) As implementações são menos importantes, pois eles podem variar.

4) O importante é resolver o problema de maneira elegante, usando a ideia por trás do padrão como um guia na implementação.

O padrão Strategy é muito útil quando temos um conjunto de algoritmos similares, 
e precisamos alternar entre eles em diferentes pedaços da aplicação. 
No exemplo do vídeo, temos diferentes maneira de calcular o imposto, 
e precisamos alternar entre elas.

O Strategy nos oferece uma maneira flexível para escrever diversos 
algoritmos diferentes, e de passar esses algoritmos para classes clientes 7
que precisam deles. Esses clientes desconhecem qual é o algoritmo "real" 
que está sendo executado, e apenas manda o algoritmo rodar. 
Isso faz com que o código da classe cliente fique bastante desacoplado 
das implementações dos algoritmos, 
possibilitando assim com que esse cliente consiga trabalhar 
com N diferentes algoritmos sem precisar alterar o seu código.

# -*- coding: UTF-8 -*-
class Orcamento(object):
  def __init__(self, valor):
    self.__valor = valor

  @property
  def valor(self):
    return self.__valor
	
class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06	
		
class Calculador_de_impostos(object):

    def realiza_calculo(self, orcamento, imposto):
        return imposto.calcula(orcamento)		
		
def main():
    print("")
    print("*"*10)
    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    print("ISS: ", calculador_de_impostos.realiza_calculo(orcamento, ISS()))
    print("ICMS: ", calculador_de_impostos.realiza_calculo(orcamento, ICMS()))
    print("*"*10)
    print("")


# Processa os dados quando acionado
if __name__ == '__main__':
    main()
		
"""
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.ex01_padrao_strategy.classes.calculador_de_impostos import Calculador_de_impostos
from src.ex01_padrao_strategy.classes.impostos import ICMS, ISS
from src.ex01_padrao_strategy.classes.orcamento import Orcamento


@fnc_decoradora_tempo_processamento
def main():
    log("")
    log("*"*10)
    orcamento = Orcamento(500.0)
    calculador_de_impostos = Calculador_de_impostos()
    log("ISS: ", calculador_de_impostos.realiza_calculo(orcamento, ISS()))
    log("ICMS: ", calculador_de_impostos.realiza_calculo(orcamento, ICMS()))
    log("*"*10)
    log("")


# Processa os dados quando acionado
if __name__ == '__main__':
    main()
