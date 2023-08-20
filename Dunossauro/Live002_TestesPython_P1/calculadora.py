from unittest import TestCase, main
# from decimal import Decimal

class Calc:
    def __int__(self):
        self.cache = 0
    def soma(self, x, y):
        if isinstance(x, int) and isinstance(y, int):
            self.cache = x + y
            return self.cache
        elif y is None:
            return x + self.cache
        else:
            raise Exception('Insira somente números!')

    def mul(self, x, y):
       if isinstance(x, int) and isinstance(y, int):
           return x * y
       else:
           raise Exception('Insira somente números!')


    def sub(self, x, y=None):
        if y is None:
            self.cache = x - self.cache
        else:
            self.cache = (x -y)
            return self.cache

    def div(self, x, y):
        return x / y

    def clear_cache(self):
        self.cache = 0
class Testes_calculadora(TestCase):
    def setUp(self):
        self.calc = Calc()

    def test_soma(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.soma(2, 2), 4)

    def test_soma_negativos(self):
        self.calc.clear_cache()
        self.assertEqual(self.calc.soma(-2, -3), -5)

    # def test_soma_float(self):
    #     self.assertEqual(self.calc.soma(2.0,3.5), 5.5)

    def test_sub(self):
        self.assertEqual(self.calc.sub(2, 2), 0)

    def test_sub_float(self):
        self.assertEqual(self.calc.sub(2.5, 1.5), 1.0)

    def test_soma_string(self):
        with self.assertRaises(Exception):
                self.calc.soma("Camila", "Helena")

    def test_sub_string(self):
        with self.assertRaises(Exception):
            self.calc.sub("Camila", "Karoline")

    def test_mul(self):
        self.assertEqual(self.calc.mul(3, 3),9)

    def test_mul_string(self):
        with self.assertRaises(Exception):
            self.calc.mul('Camila', 2)

    def test_div(self):
        self.assertEqual(self.calc.div(3, 3), 1)

    def test_div_string(self):
        with self.assertRaises(Exception):
            self.calc.div(3, "Camila")

    def test_cache_soam(self):
        self.assertEqual(self.calc.soma(self.calc.soma(2, 2)), 8)

    def test_cache_sub(self):
        """
        Explicação.

        Na primeira subtração 10 - 5, o resultado é 5.

        cache - resultado == 0
        """
        self.calc.clear_cache()
        self.assertEqual(self.calc.sub(self.calc.sub(10, 5)), 0)

if __name__ == '__main__':
    main()