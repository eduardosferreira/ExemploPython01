from abc import ABC, abstractmethod
from random import SystemRandom
from string import ascii_letters, digits


class Pessoa(ABC):
    __NR_INSTANCIA: int = 0
    __QT_DELECAO: int = 0

    @staticmethod
    def NR_INSTANCIA() -> int:
        return Pessoa.__NR_INSTANCIA
    
    def instancia(self):
        return self.__NR_INSTANCIA

    def __del__(self):
        Pessoa.__QT_DELECAO += 1

    def __new__(cls, *args, **kwargs):
        Pessoa.__NR_INSTANCIA += 1
        # SINGLETON
        # if not hasattr(cls, '_cls_exist'):
        #    cls._cls_exist = super().__new__(cls)
        # return cls._cls_exist
        return super().__new__(cls)


    @staticmethod
    def __fnc_gera_codigo_aleatorio(__p_nr_tamanho_codigo: int = 10) -> str:
        return ''.join(SystemRandom().choice(ascii_letters + digits)
                       for _ in range(__p_nr_tamanho_codigo))

    @abstractmethod
    def construtor():
        pass

    def __init__(self, __p_nm_pessoa: str = "", __p_ds_sobre_nome: str = None) -> None:
        super().__init__()
        self.nome = __p_nm_pessoa
        self.sobre_nome = (
            __p_ds_sobre_nome if __p_ds_sobre_nome is not None else "")
        self.__codigo = Pessoa.__fnc_gera_codigo_aleatorio()
        self.__NR_INSTANCIA = Pessoa.__NR_INSTANCIA

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome

    def nome_completo_formatado(self) -> str:
        return (str(self.sobre_nome.capitalize()) + ", "
                if self.sobre_nome else "") + self.nome.capitalize()

    @nome.setter
    def nome(self, __p_nm_pessoa: str):
        self.__nome: str = __p_nm_pessoa

    @property
    def sobre_nome(self) -> str:
        return self.__sobre_nome

    @sobre_nome.setter
    def sobre_nome(self, __p_ds_sobre_nome: str):
        self.__sobre_nome: str = __p_ds_sobre_nome

    @classmethod
    def nome_sobre_nome(cls, __p_nm_pessoa: str, __p_ds_sobre_nome: str):
        if not isinstance(__p_nm_pessoa, str)\
                or not __p_nm_pessoa\
                or not isinstance(__p_ds_sobre_nome, str)\
                or not __p_ds_sobre_nome:
            raise ValueError(
                f"Invalid! ({str(__p_nm_pessoa), str(__p_ds_sobre_nome)})")
        return cls(__p_nm_pessoa, __p_ds_sobre_nome)

    @classmethod
    def nome_completo(cls, __p_nm_completo: str):
        if not isinstance(__p_nm_completo, str)\
                or not __p_nm_completo\
                or len(__p_nm_completo.split(",")) <= 1\
                or not str(__p_nm_completo.split(",")[1])\
                or not str(__p_nm_completo.split(",")[0]):
            raise ValueError(
                f"Invalid! ({str(__p_nm_completo)})")
        return cls(str(__p_nm_completo.split(",")[1]), str(__p_nm_completo.split(",")[0]))

    def __eq__(self, __o: object) -> bool:
        return self.nome_completo_formatado() == self.nome_completo_formatado()

    def __str__(self) -> str:
        return f' {self.__class__.__name__} ({self.codigo}, [{self.nome_completo_formatado()}])'

    def __repr__(self) -> str:
        return "{}('{}', '{}')".format(type(self).__name__, self.nome,
                                       self.sobre_nome)

    def __setattr__(self, __name, __value) -> None:
        if __name.endswith('__nome')\
                or __name.endswith('__sobre_nome'):
            if not isinstance(__value, str)\
            or (__name.endswith('__nome') and not __value):
                raise ValueError(f"Invalid! ({str(__name)}: {str(__value)})")

        self.__dict__[str(__name)] = __value
        # print(f'__dict__[{__name}]: {self.__dict__[__name]}')
        return super().__setattr__(__name, __value)


if __name__ == '__main__':
    class C(Pessoa):
        def construtor(self):
            pass

    p1 = C("ed")
    p2 = C.nome_sobre_nome("Carlos", "Ferreira")
    p3 = C.nome_completo("Eduardo, Luiz")

    # , "p1=p2", p1.__eq__(p2), "etc..->", "p1 -> ", p1.nome, p1.sobre_nome, "p2 -> ", p2.nome, p2.sobre_nome)
    print("p1:", p1, "p2:", p2.nome_completo_formatado(), p2.instancia(), C.NR_INSTANCIA())
