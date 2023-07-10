#criar classe pessoa

class Pessoa:
    def __init__(self, nome, idade) :
        self.nome = nome
        self.idade = idade

    def falar(self):
        print("Olá, pessoal!")

class Super_Heroi(Pessoa):
    def __init__(self, nome, idade, super_poder):
        super().__init__(nome, idade)
        self.super_poder = super_poder

    def utilizar_super_poder(self):
        print("O herói utilizou o super poder: '%s'!" %self.super_poder)

joao = Pessoa("João", 18)
print(joao.nome, joao.idade)

joao.falar()

thor = Super_Heroi("Thor", 35, "Invisível")
print(thor.nome, thor.idade)

thor.falar()

thor.utilizar_super_poder()
        