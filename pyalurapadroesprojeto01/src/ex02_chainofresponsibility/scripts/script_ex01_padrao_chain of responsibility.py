# -*- coding: utf-8 -*-
"""
padrão de projeto se chama chain of responsibility, ou seja, 
chain é cadeia, 
responsibility é responsabilidade, ou seja, 
cada nó da minha cadeia tem a responsabilidade de chamar o próximo nó.

O padrão Chain of Responsibility cai como uma luva 
quando temos uma lista de comandos a serem executados de acordo com algum cenário em específico, e sabemos também qual o próximo cenário que deve ser validado, caso o anterior não satisfaça a condição.

Nesses casos, o Chain of Responsibility nos possibilita 
a separação de responsabilidades em classes pequenas e enxutas,
 e ainda provê uma maneira flexível e desacoplada de juntar esses comportamentos 
 novamente.

Será que a classe Calculador_de_descontos é realmente necessária? Discuta a utilidade dela.

RESPONDA
Opinião do instrutor

Agora que implementamos o Chain of Responsibility, temos cada uma das responsabilidades separadas em uma classe, e uma forma de unir essa corrente novamente. Veja a flexibilidade que o padrão nos deu: podemos montar a corrente da forma como quisermos, e sem muitas complicações.

Mas precisamos de uma classe que monte essa corrente na ordem certa, com todos os descontos necessários. Por isso que optamos pela classe Calculador_de_descontos. Ela poderia ter qualquer outro nome como Corrente_de_descontos, e assim por diante, mas fato é que em algum lugar do seu código você precisará montar essa corrente.

Desvantagens de Patterns
PRÓXIMA ATIVIDADE

Com certeza, com os padrões de projeto Strategy ou Chain of Responsibility o nosso código fica mais limpo do que usar um conjunto de ifs, conforme discutimos nesses capítulos. Ganhamos flexibilidade em introduzir ou tirar novas responsabilidade sem mexer no código existente. Mas qualquer mudança não só traz beneficios. Você pode pensar em alguma desvantagem? Não é necessário postar uma resposta, é mais um exercício de reflexão. Clicando em continuar você verá a opinião do instrutor.

VER OPINIÃO DO INSTRUTOR
Opinião do instrutor

Essa questão na verdade não só serve para os padrões Strategy e Chain of Responsibility como também para os outros padrões. Por exemplo, fazendo ifs na classe não é o mais flexível, no entanto é o mais fácil de entender (claro que depende da quantidade de ifs).

Os padrões de projetos tentam separar as responsabilidades para deixar o código mais flexível, mas introduzem uma indireção, eles delegam o trabalho para outras classes que pode deixar o código mais complexo e difícil de entender. Na hora de aplicar o padrão sempre coloque esse questão na ponta de língua e tente avaliar se realmente vale a pena.

# no arquivo descontos.py, última classe

class Sem_desconto(object):

  def calcula(self, orcamento):

    return 0

# -*- coding: UTF-8 -*-
# calculador_de_descontos.py
from descontos import Desconto_por_cinco_itens, Desconto_por_mais_de_quinhetos_reais, Sem_desconto

class Calculador_de_descontos(object):

    def calcula(self, orcamento):

        desconto = Desconto_por_cinco_itens(
            Desconto_por_mais_de_quinhentos_reais(
                Sem_desconto()
            )
        )

        return desconto

if __name__ == '__main__':

    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))

    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    print 'Desconto calculado : %s' % (desconto)


Chain of Responsibility em Python
O Chain of Responsibility é um padrão de projeto comportamental que permite passar a solicitação ao longo da cadeia de handlers em potencial até que um deles lide com a solicitação.

O padrão permite que vários objetos tratem a solicitação sem acoplar a classe remetente às classes concretas dos destinatários. A cadeia pode ser composta dinamicamente em tempo de execução com qualquer handler que siga uma interface de handler padrão.

Uso do padrão em Python
Complexidade: 

Popularidade: 

Exemplos de uso: O padrão Chain of Responsibility não é um padrão frequente em um programa Python, pois é relevante apenas quando o código opera com cadeias de objetos.

Identificação: O padrão é reconhecível pelos métodos comportamentais de um grupo de objetos que indiretamente chamam os mesmos métodos em outros objetos, enquanto todos os objetos seguem a interface comum.

Exemplo conceitual
Este exemplo ilustra a estrutura do padrão de projeto Chain of Responsibility. Ele se concentra em responder a estas perguntas:

De quais classes ele consiste?
Quais papéis essas classes desempenham?
De que maneira os elementos do padrão estão relacionados?
 main.py: Exemplo conceitual
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
All Concrete Handlers either handle a request or pass it to the next handler in
the chain.
"""


class MonkeyHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None:
    """
    The client code is usually suited to work with a single handler. In most
    cases, it is not even aware that the handler is part of a chain.
    """

    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog)

    # The client should be able to send a request to any handler, not just the
    # first one in the chain.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel)
 Output.txt: Resultados da execução
Chain: Monkey > Squirrel > Dog

Client: Who wants a Nut?
  Squirrel: I'll eat the Nut
Client: Who wants a Banana?
  Monkey: I'll eat the Banana
Client: Who wants a Cup of coffee?
  Cup of coffee was left untouched.

Subchain: Squirrel > Dog

Client: Who wants a Nut?
  Squirrel: I'll eat the Nut
Client: Who wants a Banana?
  Banana was left untouched.
Client: Who wants a Cup of coffee?
  Cup of coffee was left untouched.

"""
import __init__
from src.util.comum import log, fnc_decoradora_tempo_processamento
from src.ex02_chainofresponsibility.classes.orcamento import Orcamento
from src.ex02_chainofresponsibility.classes.item import Item
from src.ex02_chainofresponsibility.classes.calculador_de_descontos\
    import Calculador_de_descontos


@fnc_decoradora_tempo_processamento
def main():
    log("")
    log("*"*10)

    orcamento = Orcamento()
    orcamento.adicionar(Item('Item A', 100.0), Item('Item B', 50.0))
    orcamento.adicionar(Item('Item C', 400.0))
    calculador_de_descontos = Calculador_de_descontos()
    desconto = calculador_de_descontos.calcula(orcamento)
    for item in sorted(orcamento.listagem(), reverse=True):
        log(item)
    log(f'Desconto calculado : {desconto:.2f}')
    # imprime 38.5

    log("*"*10)
    log("")


# Processa os dados quando acionado
if __name__ == '__main__':
    main()
