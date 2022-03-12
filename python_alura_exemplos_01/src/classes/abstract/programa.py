from abc import ABC, abstractmethod
from functools import reduce
from random import SystemRandom
from string import ascii_letters, digits


class Programa(ABC):
    NR_INSTANCIA = 0

    def __new__(cls, *args, **kwargs):
        Programa.NR_INSTANCIA += 1
        return super().__new__(cls)

    def __del__(self):
        Programa.NR_INSTANCIA -= 1

    @staticmethod
    def __gerador_codigo_aleatorio(__tamanho_codigo: int = 10) -> str:
        return ''.join(SystemRandom().choice(ascii_letters + digits)
                       for _ in range(__tamanho_codigo))

    @abstractmethod
    def __init__(self, __nome: str, __ano: int, __codigo: str = None):
        self.codigo = Programa.__gerador_codigo_aleatorio()\
            if __codigo is None else __codigo
        self.nome = __nome
        self.nome = self.nome.title()
        self.ano = __ano
        self._likes = 0
        self.__instancia = Programa.NR_INSTANCIA

    @classmethod
    def contrutor_codigo(self, __nome: str, __ano: int, __codigo: str):
        self().__init__(__nome, __ano, __codigo)

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, __codigo: str):
        self.__codigo = __codigo

    def __setattr__(self, __name: str, __value):
        if str(__name).strip().endswith('ano')\
                or str(__name).strip().endswith('__instancia'):
            if not isinstance(__value, int) or not __value:
                raise ValueError(
                    f'Invalid [int]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value

        if str(__name).strip().endswith('_likes'):
            if not isinstance(__value, int):
                raise ValueError(
                    f'Invalid [int]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value
        
        if str(__name).strip().endswith('nome')\
                or str(__name).strip().endswith('codigo'):
            if not isinstance(__value, str) or not __value:
                raise ValueError(
                    f'Invalid [str]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value

        return super().__setattr__(__name, __value)

    def __str__(self):
        return "\n-> "\
            + str(self.__instancia).rjust(20, '0') + ") " \
            + str(self.__class__.__name__) \
            + " >> \n" \
            + '\n'.join([f'[{str(k)}]: {str(v)}'
                         for k, v in self.__dict__.items()])

    @staticmethod
    def eh_igual(__cls: object, __o: object) -> bool:
        try:
            if str(__cls.__class__.__name__) ==\
               str(__o.__class__.__name__):
                return \
                    reduce(lambda y, z: False
                           if not y or not z else True,
                           [__o.__dict__[k] == v
                            for k, v in __cls.__dict__.items()
                            if not str(k).strip().endswith('codigo')
                            and not str(k).strip().endswith('_likes')
                            and not str(k).strip().endswith('__instancia')
                            and not isinstance(v, list)
                            ])
            return False
        except Exception:
            return False

    def __eq__(self, __o: object) -> bool:
        return Programa.eh_igual(self, __o)
