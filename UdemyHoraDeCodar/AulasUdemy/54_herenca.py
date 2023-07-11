#orientação a objetos: herança

class Veiculo:
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print("Veículo ligado!")

#Herança de 'Veículo' para a classe 'Carro'
class Carro(Veiculo):
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca)
        self.teto_solar = teto_solar


polo = Carro(4, "VW", True)
print(polo.marca)

polo.ligar()

print(polo.teto_solar)

class Moto(Veiculo):
    def __init__(self, rodas, marca, protecao_lateral):
        super().__init__(rodas, marca)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        print("Empinou a moto!")

moto = Moto(2, "Honda", False)        

print(moto.rodas)

#metodo da classe pai
moto.ligar()

#metodo da própria classe moto
moto.empinar()