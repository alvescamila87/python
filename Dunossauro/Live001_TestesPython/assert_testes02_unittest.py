# Utilizando o framework Unittest

from unittest import TestCase, main
def soma(x, y):
    return x + y

def sub(x, y):
    return  x - y

def mul(x, y):
    return x * y


class Testes(TestCase):
    def test_soma(self):
        self.assertEqual(soma(5,5),10)

    # def test_soma_errada(self):
    #     self.assertEqual(soma(5,5), 11)

    def test_soma_menor(self):
        self.assertLess(soma(5,5), 11) # assert 10 < 11


    def test_soma_menor_igual(self):
        self.assertLessEqual(soma(5,5), 10) # assert 10 <= 10

    def test_sub(self):
        self.assertEqual(sub(3,3),0) # assert 3 == 3

    # def test_sub_errada(self):
    #     self.assertEqual(sub(8,7), -1)

if __name__ == '__main__':
    main()