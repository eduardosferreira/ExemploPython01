def fnc_fatorial(p_nr):

    if p_nr < 0:
        return 0
    
    nr_aux = nr_fat = int(1)

    while nr_aux <= p_nr:
        nr_fat *= nr_aux
        nr_aux += 1

    return nr_fat

def test_fatoria_01():
    assert fnc_fatorial(0) == 1

def fatoria_01_test():
    assert fnc_fatorial(0) == 1

def test_fatoria_negativo():
    assert fnc_fatorial(-10) == 0

def test_fatoria_04():
    assert fnc_fatorial(4) == 24

def test_fatoria_05():
    assert fnc_fatorial(5) == 120
    
