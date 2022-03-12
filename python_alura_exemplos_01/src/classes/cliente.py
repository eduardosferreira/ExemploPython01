import __init__
from src.classes.abstract.pessoa import Pessoa


class Cliente(Pessoa):
    def construtor(self):
            pass


if __name__ == '__main__':
    #p0 = Pessoa()
    p1 = Cliente("ED")
    p2 = Cliente("ED")
    print(p1.nome, p2, p1.__eq__(p2))
