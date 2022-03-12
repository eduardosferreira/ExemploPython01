import abc


class Base(abc.ABC):

    @abc.abstractmethod
    def _sentinel(self): pass

    def __init_subclass__(cls, *args, **kw):
        # Injeta um método só para sobre-escrever o abstract-method:
        cls._sentinel = lambda self: None


class B(Base):
    def __init__(self) -> None:
        super().__init__()
        print("oi")


class Mother:
    def __init__(self, a, b, c):
        if self.__class__ is Mother:
            raise TypeError("Mother class cannot be instantiated")
        self.a = a
        self.b = b
        self.c = c


class Daughter(Mother):
    pass


if __name__ == '__main__':
    b = B()
    # a = Base()
    Daughter(1, 2, 3)  # funciona
    # Mother(1, 2, 3)  # produz um TypeError
