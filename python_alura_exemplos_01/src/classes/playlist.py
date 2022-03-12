import __init__
from src.classes.abstract.programa import Programa
from src.classes.listaIterator import ListaIterator


class Playlist(ListaIterator):
    def __init__(self, __nome_play_list, *args):
        super().__init__()
        self.nome_play_list = __nome_play_list
        self.adicionar_lista(*args)
        if not self.validar_attribuicao_lista(Programa):
            raise ValueError(
                f'Invalid [list/Programa]!\
                {str(__class__.__name__)} >> \
                {str(self.__class__.__name__)} >> \
                lista_iterator  >> {str(self.lista_iterator)}')


    def __setattr__(self, __name: str, __value):
        if str(__name).strip().endswith('nome_play_list'):
            if not isinstance(__value, str):
                raise ValueError(
                    f'Invalid [str]!  {str(__class__.__name__)} >> {str(self.__class__.__name__)} >> {str(__name)}  >> {str(__value)}')
            self.__dict__[__name] = __value
        if str(__name).strip().endswith('lista_iterator'):
            self.__dict__[__name] = __value
        return super().__setattr__(__name, __value)


if __name__ == '__main__':
    import itertools
    from src.classes.filme import Filmes
    from src.classes.series import Series
    from src.classes.cliente import Cliente
    c1 = Cliente("edu", "ferr")
    f1 = Filmes("F1", 1, 10)
    f1.dar_likes()
    f1.dar_likes()
    f1.dar_likes()
    f2 = Filmes("F2", 2, 20)
    s1 = Series("S1", 3, 30)
    s2 = Series("S2", 4, 40)
    s2.dar_likes()
    # p2 = Playlist("lista2", f1)
    # p3 = Playlist("lista1", f1, f2, s1, s2)
    p1 = Playlist("P.lista....", f2, s1, f1, s2)
    i1, i2, i3 = itertools.tee(p1, 3)
    print(p1, p1.tamanho)
    print('0.1',len(p1))
    print('0.1', [x.nome for x in i1],len(p1))
    print('0.2', [x.nome for x in i2],len(p1))
    print('1.', p1[-1].nome, len(p1))
    print('2.', p1.next().nome, len(p1))
    print('2.1', s1 in p1, len(p1))
    print('2.2', s2 in p1, len(p1))
    print('0.3', [x.nome for x in i3],len(p1))
    print('3.', p1[-1].nome, len(p1))
    
    for __programa in p1:  # .lista_iterator:
        print('4.', __programa.nome)
        #, len(p1.lista_iterator),
        #      .nome_play_list, len(p1.lista_iterator), __programa.__eq__(f1))
        # , p1.nome_play_list, __programa.nome,
        #  f1 in p1,
        #  s2 in p1,
        #  s1 in p1,
        #  f2 in p1,
        #  __programa.__eq__(s2), __programa.__eq__(s1),
        #  len(p1.lista_iterator))
