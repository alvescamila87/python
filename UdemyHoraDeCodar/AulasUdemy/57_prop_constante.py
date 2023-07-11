#orientação a objetos: propriedades constantes

class Carro:
   
    rodas = 4 #propriedade constante, declarado fora de self

    def __init__(self, marca):
        self.marca = marca

polo = Carro("Polo")

print(polo.marca)
print(polo.rodas)
