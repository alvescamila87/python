#orientacao a objetos: objeto

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

#instanciando objeto / criando objeto a partir da classe "Pessoa"
camila = Pessoa("Camila", 35, "Desenvolvedora")

print(camila)

print(type(camila))

#acessar as propriedades (anotação de pontos), assim é possível acessar o valor daquela propriedade
print(camila.nome)
print(camila.idade)
print(camila.profissao)

if camila.nome == "Camila":
    print("O nome é Camila")

nome = camila.nome
print(nome)