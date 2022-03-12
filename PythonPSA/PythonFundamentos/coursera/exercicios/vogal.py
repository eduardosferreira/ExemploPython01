def vogal(p_str_caracter):

    if str(p_str_caracter) in "AEIOUaeiou" \
       and len(str(p_str_caracter).strip()) == 1:
        return True
    
    return False


def test_vogal_01():
    assert vogal("A")

def test_vogal_02():
    assert vogal("a")
    
def test_vogal_03():
    assert not vogal("b")

def test_vogal_04():
    assert not vogal("aa")

def test_vogal_05():
    assert vogal("e")    

def test_vogal_06():
    assert not vogal(1)