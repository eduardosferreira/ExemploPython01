from abc import ABCMeta, abstractmethod


class ListaIterator(metaclass=ABCMeta):
    @staticmethod
    def metodo_estatico():
        return "ListaIterator"

    def __init__(self):
        self.__lista = []

    @property
    def lista(self):
        return tuple(self.__lista)

    def hashNext(self) -> bool:
        if self.__lista is None or len(self.__lista) == 0:
            return False
        return True

    def __next__(self):
        if not self.hashNext():
            self.__lista = None
            raise StopIteration
        value = self.__lista.pop()
        return value

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self.__lista.__iter__()

    def __getitem__(self, items):
        try:
            return self.__lista[items]
        except Exception:
            return []

    def __len__(self):
        try:
            return len(self.__lista)
        except Exception:
            return 0

    def __str__(self):
        string_list = "["
        if self.__lista is not None:
            string_list += ';\n'.join([f'[{str(n)}] : {str(x)} \n' for n,
                                      x in enumerate(self.__lista)])
        string_list += "]"
        return string_list

    def __setattr__(self, __name: str, __value):
        if str(__name).strip().endswith('__lista'):
            if not isinstance(__value, list) and __value is not None:
                raise ValueError(
                    f'Invalid [list]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value
        return super().__setattr__(__name, __value)

    @abstractmethod
    def adicionar(self, *args, **kwargs):
        def __fnc_value(__value):
            if isinstance(__value, (list, tuple, set)):
                self.__lista.extend((x for x in __value))
            else:
                self.__lista.append(__value)
        for value in args:
            __fnc_value(value)
        for _, value in kwargs.items():
            __fnc_value(value)

    def listagem(self):
        return tuple(self.__lista)

    @property
    def tamanho(self):
        return len(self.__lista)
