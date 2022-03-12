def fnc_primo(p_nr):
    
    nr_aux = 2

    while nr_aux * nr_aux <= p_nr:
        if (p_nr % nr_aux) == 0:
            return False
        nr_aux += 1

    return True

def maior_primo(p_nr):

    if p_nr < 2:
        return None
    
    nr_aux = p_nr

    while nr_aux > 2:
        if fnc_primo(nr_aux):
            return nr_aux
        nr_aux -= 1

    return 2

def test_maior_primo_01():
    assert maior_primo(100) == 97

def test_maior_primo_02():
    assert maior_primo(7) == 7
    
def test_maior_primo_03():
    assert maior_primo(1) is None
