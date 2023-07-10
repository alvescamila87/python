#criar classe mamífero, herde detalhes da classe, crie objetos nas classes que herdaram e imprima

class Mamifero:
    def __init__ (self, mama, raca):
        self.mama = mama
        self.raca = raca

    def andar(self):
        print("O mamífero andou")

class Cachorro(Mamifero):
    def __init__(self, mama, raca, late):
        super().__init__(mama, raca)
        self.late = late

    def latir(self):
        print("Au, au... Laiu")

class Gato(Mamifero):
    def __init__(self, mama, raca, mia):
        super().__init__(mama, raca)
        self.mia = mia

    def miar(self):
        print("Meoww... Miou")

mamifero_1 = Mamifero(True, "Cachorro") 
print(mamifero_1.mama, mamifero_1.raca)

mamifero_1.andar()

cachorro = Cachorro(True, "Pinscher", True)
print(cachorro.mama, cachorro.raca, cachorro.late)

cachorro.andar()
cachorro.latir()

gato = Gato(True, "Persa", True)
print(gato.mama, gato.raca, gato.mia)

gato.andar()
gato.miar()
    
        