# -*- coding: utf-8 -*-
"""Classe de Pessoa
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from functools import total_ordering
from random import SystemRandom
from string import ascii_letters, digits


@total_ordering
class Pessoa(ABC):
    """Classe ABSTRATA Pessoa
    """
    __codigo: str = ""
    __nome: str = ""
    __data_atualizacao: datetime = datetime.now()
    __data_cadastro: datetime = datetime.now()
    INSTANCIA: int = 0
    QT_INSTANCIA: int = 0

    def __repr__(self) -> str:
        """Retorna a descricao e atributos da classe
        """
        return "{}('{}')".format(type(self).__name__, self.__nome)

    def __str__(self) -> str:
        """Retorna os atributos da classe
        """
        return f'[{self.INSTANCIA}] Classe {type(self).__name__}'\
            f', ('\
            f'  Codigo: {self.codigo}'\
            f', Nome: {self.nome}'\
            f', Data Cadastro: {self.data_cadastro}'\
            f', Data Atualização: {self.data_atualizacao}'\
            f'  )'

    def __eq__(self, __o: object) -> bool:
        """Retorna a equilizacao dos objetos da classe
        """
        if not isinstance(__o, Pessoa):
            return NotImplemented
        if __o.codigo == self.codigo and __o.nome == self.nome:
            return True
        return False

    def __lt__(self, __o) -> bool:
        """Retorna a equilizacao dos objetos da classe refere >
        """
        if not isinstance(__o, Pessoa):
            return NotImplemented
        if __o.codigo == self.codigo and __o.nome == self.nome:
            return int(self.INSTANCIA) < int(__o.INSTANCIA)
        elif __o.codigo != self.codigo:
            return __o.codigo < self.codigo
        return __o.nome < self.nome

    def __setattr__(self, __name: str, __value) -> None:
        """Valida os dados atribuidos
        """
        if __name.endswith('__codigo')\
                or __name.endswith('__nome'):
            if not isinstance(__value, str):
                raise ValueError(
                    f"ERRO: Dados incorreto! [{__name}]:{__value}")
            self.__dict__[__name] = __value

        if __name.endswith('__data_atualizacao')\
                or __name.endswith('__data_cadastro'):
            if not isinstance(__value, datetime) or not __value:
                raise ValueError(
                    f"ERRO: Dados incorreto! [{__name}]:{__value}")
            self.__dict__[__name] = __value

        return super().__setattr__(__name, __value)

    @abstractmethod
    def imprimir(self):
        """Funcao abstrata a ser construido para quem herdar
        """
        return self.__repr__()

    def __new__(cls: type[Pessoa], *args, **kwargs) -> Pessoa:
        """Antes de instanciar o contrutor, valida informacoes
        """
        # if not hasattr(cls, '__existe'):
        cls.__existe = super().__new__(cls)
        Pessoa.INSTANCIA += 1
        Pessoa.QT_INSTANCIA += 1
        return cls.__existe

    def __del__(self):
        """Deleta / Apaga os objetos da classe
        """
        Pessoa.QT_INSTANCIA -= 1

    @staticmethod
    def funcao_geracao_codigo(p_nr_tamanho_codigo: int = 10) -> str:
        """ Retorna codigo aleatorio
        """
        return ''.join(SystemRandom().choice(ascii_letters + digits)
                       for _ in range(p_nr_tamanho_codigo))

    def __init__(self, nome: str = ""):
        """Construtor da Classe
        """
        if type(self) == Pessoa:
            raise TypeError("Classe abstrata, não pode instanciar")

        self.__nome = nome
        self.__data_atualizacao: datetime = datetime.now()
        self.__data_cadastro: datetime = datetime.now()
        self.__codigo = Pessoa.funcao_geracao_codigo()
        self.INSTANCIA = Pessoa.INSTANCIA

    @classmethod
    def construtor_codigo_nome(cls: type[Pessoa],
                               codigo: str, nome: str) -> Pessoa:
        """Construtor da classe, por nome e codigo
        """
        instancia_classe = cls(nome)
        instancia_classe.__codigo = codigo
        instancia_classe.atualiza_data()
        return instancia_classe

    def atualiza_data(self):
        """Atualiza a data
        """
        self.data_atualizacao = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    @property
    def nome(self):
        """Retorna atributo nome
        """
        return self.__nome.strip()

    @property
    def codigo(self):
        """Retorna atributo codigo
        """
        return self.__codigo

    @property
    def data_cadastro(self) -> str:
        """Retorna o atributo data no formato dd/mm/yyyy hh:mi:ss
        """
        return self.__data_cadastro.strftime('%d/%m/%Y %H:%M:%S')

    @property
    def data_atualizacao(self) -> str:
        """Retorna o atributo data no formato dd/mm/yyyy hh:mi:ss
        """
        return self.__data_atualizacao.strftime('%d/%m/%Y %H:%M:%S')

    @data_atualizacao.setter
    def data_atualizacao(self, data: str):
        """Atribui o atributo data
        """
        self.__data_atualizacao = datetime.strptime(data, '%d/%m/%Y %H:%M:%S')


if __name__ == '__main__':
    from typing import List
    import pprint

    class B(Pessoa):
        def imprimir(self):
            return super().imprimir()
    # breakpoint()
    lista: List[Pessoa] = [B("Eduardo"),
                           B().construtor_codigo_nome(
        "10", "Eduardo"),
        B().construtor_codigo_nome("10", "Eduardo")]
    print()
    pprint.pprint(B("teste").__dict__, indent=2)
    print()
    pprint.pprint(lista, width=5)
    print()
    for item in lista:
        print()
        print(item)
    print()

    for item in sorted(lista, reverse=True):
        print()
        print(item)
    print()
