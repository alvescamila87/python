#orientação a objeto: metodo

class Carro:
    km = 0

    def __init__(self, marca, valor, portas, tanque_gasolina):
        self.marca = marca
        self.valor = valor
        self.portas = portas
        self.tanque_gasolina = tanque_gasolina

    def abastecer(self, litros):
        if self.tanque_gasolina >= 100:
            print("Taque cheio: %d" %litros)
        else:
            self.tanque_gasolina += litros
            if self.tanque_gasolina > 100:
                self.tanque_gasolina = 0

    def dirigir(self, km):
        km_por_litro = 10
        self.tanque_gasolina -= (km / km_por_litro)


fusca = Carro("Fusca", 20000, 2, 10)
print(fusca.tanque_gasolina)

#abastecer tanque
fusca.abastecer(50)
print(fusca.tanque_gasolina)

#dirigir para esvaziar tanque
fusca.dirigir(80)
print(fusca.tanque_gasolina)