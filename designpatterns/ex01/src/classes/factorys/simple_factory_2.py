"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.

Vantagens:
    Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.

    Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).

    Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.

Desvantagens:
    Podem introduzir muitas classes no código

Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory

Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod
from typing import List, Union
from constantes_simple_factory_2 import (CARRO_LUXO,
                                         CARRO_POPULAR, MOTO_POPULAR,
                                         MOTO_LUXO)


class Veiculo(ABC):
    __codigo: int = 0
    __descricao: str = ""

    def __init__(self, codigo: int = 0, descricao: str = "") -> None:
        super().__init__()
        self.__codigo = codigo
        self.__descricao = descricao

    @classmethod
    def carregar_nome_codigo_veiculo(cls,
                                     codigo: int = 0,
                                     descricao: str = "") -> object:
        return cls(codigo, descricao)

    @abstractmethod
    def buscar_cliente(self) -> None: pass

    @property
    def veiculo(self):
        return (self.__descricao.capitalize()
                if self.__descricao else self.__class__.__name__
                )


class CarroPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro popular está buscando o cliente...', self.veiculo)


class CarroLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Carro de luxo está buscando o cliente...', self.veiculo)


class MotoLuxo(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto está buscando o cliente...', self.veiculo)


class MotoPopular(Veiculo):
    def buscar_cliente(self) -> None:
        print('Moto popular está buscando o cliente...', self.veiculo)


class VeiculoFactory:

    @staticmethod
    def get_carro(tipo: str) -> Union[CarroLuxo, CarroPopular, MotoPopular,
                                      MotoLuxo]:
        if tipo == CARRO_LUXO:
            return CarroLuxo()
        if tipo == CARRO_POPULAR:
            return CarroPopular()
        if tipo == MOTO_POPULAR:
            return MotoPopular()
        if tipo == MOTO_LUXO:
            return MotoLuxo()
        assert 0, 'Veículo não existe'

    def __init__(self, tipo: str) -> None:
        self.carro = self.get_carro(tipo)

    def buscar(self) -> None:
        self.carro.buscar_cliente()


def main(*args, **kargs):
    from random import choice
    carros_disponiveis: List(str) = []
    carros_disponiveis = ['luxo', 'popular', 'moto', 'rx']

    for i in range(10):
        carro = VeiculoFactory(choice(carros_disponiveis))
        carro.buscar()


if __name__ == "__main__":
    main()
