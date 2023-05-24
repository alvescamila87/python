def vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if x in vogais:
        return True
    else:
        return False

def test_vogala():
    assert vogal('a') == 'a'

def test_vogalB():
    assert vogal('B') == 'B'



