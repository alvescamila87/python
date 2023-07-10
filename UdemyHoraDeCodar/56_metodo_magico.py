#orientação a objetos: metodo mágico

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return "O nome é %s, tem %d anos e é um %s." %(self.nome, self.idade, self.profissao)
    

joao = Pessoa("Joao", 21, "Empresário")

#invocando o método, tem que colocar na função de print, pois é uma string por meio de um return
print(joao.__str__())