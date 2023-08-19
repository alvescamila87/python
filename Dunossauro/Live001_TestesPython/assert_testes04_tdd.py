# Utilizando o framework Unittest + TDD

from unittest import TestCase, main

def eh_par(valor: int) -> bool:
    """
    Função que verifica se o número é par
    :param valor: valor de entrada do tipo integer ou float
    :return: retorna True se valor é par, senão retorna False.
    """
    if isinstance(valor, int) or isinstance(valor, float):
        return True if valor % 2 == 0 else False
    else:
        return False

# TDD
class Testes(TestCase):
    def test_par(self):
        self.assertEqual(eh_par(2), True)

    def test_impar(self):
        self.assertEqual(eh_par(3), False)

    def test_string(self):
        self.assertEqual(eh_par('string'), False) #TypeError

    def test_float(self):
        self.assertEqual(eh_par(4.5), False)

if __name__ == '__main__':
    main()