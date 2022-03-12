# -*- coding: utf-8 -*-
"""
O princípio de Hollywood
PRÓXIMA ATIVIDADE

Repare que no padrão Template method a classe mãe controla os filhos. Os filhos preenchem apenas as lacunas da mãe, aquele métodos abstratos, mas a classe mãe está no poder e chama estes métodos dos filhos.

Esse fato que filhos não ficam mais no controle da execução também é chamado de The Hollywood Principle. Esse princípio diz: “Don't call us, we'll call you”! Ou seja, invés você (os filhos) ficarem chamando a classe pai, o controle é invertido e a classe mãe chama os filhos.

A ideia de inverter o controle (IoC - Inversion of Control) vai muito mais longe e não é usado apenas no Template Method. Você sabe mais algum lugar onde a inversão de controle é aplicado? Pesquise :)

A inversão de controle é um princípio fundamental no desenvolvimento e é utilizado em qualquer framework ou container. No Django, por exemplo, você consegue com poucas classes e funções criar aplicações complexas pois tem inversão de controle! O Django chama as suas funções, ou seja, ele esta no poder e segue o Principio de Hollywood.

Se não tivesse a ajuda do Django e a inversão de controle, o desenvolvedor seria responsável em fazer o parsing dos cabeçalhos HTTP, mapear uma URL para uma função, abrir e fechar a conexão e transação, fazer o tratamento de erro, renderizar a resposta etc etc etc .... Tudo isso o Django prepara antes de chamar o código da aplicação. Falando um pouco simplificado, o Django é o template, a grande mãe que prepara tudo para o nosso código ficar o mais simples possível.

"""
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.ex03_templatemethod.classes.orcamento import Orcamento
from src.ex03_templatemethod.classes.item import Item
from src.ex03_templatemethod.classes.calculador_de_descontos\
    import Calculador_de_descontos
from src.ex03_templatemethod.classes.calculador_de_impostos\
    import Calculador_de_impostos
from src.ex03_templatemethod.classes.impostos\
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
    log(calculador_de_impostos.realiza_calculo(orcamento, ICPP())) # imprime 25.0
    log(calculador_de_impostos.realiza_calculo(orcamento, IKCV())) # imprime 30.0
    log("*"*10)
    log("")


# Processa os dados quando acionado
if __name__ == '__main__':
    main()
