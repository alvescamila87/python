#orientação a objetos: substituicao de método

class Pessoa:
    def falar(self):
        print("Olá, pessoal!")

#classe filha
class Joao(Pessoa):
    def falar(self):
        print("Olá, pessoal! Me chamo João :)")


class Pedro(Pessoa):
    pass

#invocar a classe
joao = Joao()

#chamar método
joao.falar()

pedro = Pedro()

pedro.falar()