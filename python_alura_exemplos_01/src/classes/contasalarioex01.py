from functools import total_ordering
from operator import attrgetter
from copy import deepcopy

@total_ordering
class ContaSalarioEx01:
    nr_intancia = 0

    def __new__(cls, *args, **kwargs):
        ContaSalarioEx01.nr_intancia += 1
        return super().__new__(cls)

    def __init__(self, codigo, saldo=None):
        self._codigo = codigo
        self._saldo = 0 if saldo is None\
            or not isinstance(saldo, (int, float))\
            or saldo <= 0 else saldo
        self._nr_intancia = ContaSalarioEx01.nr_intancia

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[{} >>Codigo {} Saldo {}<<]".format(self._nr_intancia,
                                                    self._codigo, self._saldo)

    def __eq__(self, __o):
        if(type(__o) != ContaSalarioEx01):
            return False

        return self._codigo == __o._codigo\
            and self._saldo == __o._saldo

    def __lt__(self, __o):
        if self._saldo == __o._saldo and self._codigo == __o._codigo:
            return int(self._nr_intancia) < int(__o._nr_intancia)
        elif self._saldo == __o._saldo:
            return self._codigo < __o._codigo
        else:
            return self._saldo < __o._saldo


if __name__ == '__main__':
    pass
    e1 = ContaSalarioEx01(1, 100)
    e2 = ContaSalarioEx01(2, 100.1)
    e21 = ContaSalarioEx01(3, 100.1)
    e31 = ContaSalarioEx01(3, 100.1)
    e3 = ContaSalarioEx01(11, 10.1)
    e4 = ContaSalarioEx01(12, 10)
    e5 = ContaSalarioEx01(12, 10)
    e6 = ContaSalarioEx01(12, 10)
    e7 = deepcopy(e1)

    l0 = [e6, e21, e1, e3, e2, e5, e31, e4, e7]
    l1 = sorted(l0)
    #l2 = sorted(l0, key=attrgetter("_codigo"))
    #l3 = sorted(l0, key=attrgetter("_saldo", "_codigo"))
    # print()
    # for conta in l0:
    #    print(conta)
    print()
    for conta in l1:
        print(conta)
    print(e5 < e4, e5 < e6, e4 < e6, e7 <= e1)
    # for conta in l2:
    #    print(conta)
    # print()
    # for conta in l3:
    #    print(conta)
    # print()

"""

"""