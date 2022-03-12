class ListaIterator:

    def __init__(self):
        self.lista_iterator = list()

    def hashNext(self) -> bool:
        if self.lista_iterator is None or len(self.lista_iterator) == 0:
            return False
        return True

    def __next__(self):
        if not self.hashNext():
            self.lista_iterator = None
            raise StopIteration
        value = self.lista_iterator.pop()
        return value

    def next(self):
        return self.__next__()

    def __iter__(self):
        return self.lista_iterator.__iter__()

    def __getitem__(self, items):
        try:
            return self.lista_iterator[items]
        except Exception:
            return []

    def __len__(self):
        try:
            return len(self.lista_iterator)
        except Exception:
            return 0

    def __str__(self):
        string_list = "["
        if self.lista_iterator is not None:
            string_list += ';\n'.join([f'[{str(n)}] : {str(x)} \n' for n,
                                      x in enumerate(self.lista_iterator)])
        string_list += "]"
        return string_list

    def __setattr__(self, __name: str, __value):
        if str(__name).strip().endswith('lista_iterator'):
            if (not isinstance(__value, list)
                    and __value is not None):
                raise ValueError(
                    f'Invalid [list]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value
        return super().__setattr__(__name, __value)

    def validar_attribuicao_lista(self, __o):
        if not isinstance(self.lista_iterator, list)\
                and self.lista_iterator is not None:
            return False
        if self.lista_iterator is not None:
            for __item in self.lista_iterator:
                if not isinstance(__item, __o):
                    return False
        return True

    def adicionar_lista(self, *args, **kwargs):
        def __fnc_value(__value, __lista_iterator):
            if isinstance(__value, (list, tuple, set)):
                __lista_iterator.extend((x for x in __value))
            else:
                __lista_iterator.append(__value)
        for value in args:
            __fnc_value(value, self.lista_iterator)
        for _, value in kwargs.items():
            __fnc_value(value, self.lista_iterator)

    @property
    def listagem(self):
        return self.lista_iterator

    @property
    def tamanho(self):
        return len(self.lista_iterator)
