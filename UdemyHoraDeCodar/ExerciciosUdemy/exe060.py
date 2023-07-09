#orientação a objetos: criar classe carro e objeto de com os valores das propriedades

class Carro:
    def __init__(self, portas, motor, teto_solar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.teto_solar = teto_solar
        self.marca = marca
        self.preco = preco

carro_1 = Carro(4, 2.0, True, "BMW", 150000)
print(carro_1.marca, carro_1.preco, carro_1.motor,carro_1.teto_solar,carro_1.portas)

carro_2 = Carro(2, 1.0, False, "Fusca", 20000)
print(carro_2.marca, carro_2.preco)