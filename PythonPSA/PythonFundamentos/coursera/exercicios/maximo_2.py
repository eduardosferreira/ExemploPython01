def maximo(p_nr_1,p_nr_2):
    if p_nr_1 >= p_nr_2:
        return p_nr_1
    else:
        return p_nr_2

def test_maximo_01():
    assert maximo(3,4) == 4

def test_maximo_02():
    assert maximo(0,-1) == 0
    
def test_maximo_02():
    assert maximo(-1,-1) == -1
