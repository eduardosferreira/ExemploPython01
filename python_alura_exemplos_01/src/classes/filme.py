import __init__
from src.classes.abstract.programa import Programa


class Filmes(Programa):
    def __init__(self, __nome: str, __ano: int, __duracao: int):
        super().__init__(__nome, __ano)
        self.duracao = __duracao

    def __setattr__(self, __name: str, __value):
        if str(__name).strip().endswith('duracao'):
            if not isinstance(__value, int) or not __value:
                raise ValueError(
                    f'Invalid [int]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value
        return super().__setattr__(__name, __value)

    def __str__(self):
        return super().__str__()

    def __eq__(self, __o: object) -> bool:
        return super().__eq__(__o)
