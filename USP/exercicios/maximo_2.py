def maximo(x, y):
    if x < y:
        return y
    else:
        return x

def test_maximo2e4():
    assert maximo(2, 4) == 4

def test_maximo2e_4():
    assert maximo(2, -4) == 2

def test_maximo4e2():
    assert maximo(4, 2) == 4

def test_maximo7e7():
    assert maximo(7, 7) == 7

def test_maximo100e350():
    assert maximo(100, 350) == 350