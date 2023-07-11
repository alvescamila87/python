#orientação a objetos: método

class Carro:
    def __init__(self, marca, preco):
        self.marca = marca
        self.preco = preco

    #metodo
    def ligar(self):
        print("Vrummm")

    #medoto para alterar outro já existente
    def mudar_preco(self, novo_preco):
        self.preco = novo_preco

polo = Carro("VW", 75000)
print(polo.marca)

#chamando a funcao do metodo ligar
polo.ligar()

#chamando a funcao do metodo mudança de preço
polo.mudar_preco(85000)
print(polo.preco)