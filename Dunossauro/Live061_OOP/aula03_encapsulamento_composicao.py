# Encapsulamento, Composicao, Dunders (métodos mágicos) e Super

# 1) Encapsulamento: agrupar dados e subrotinas e ocultar dados irrelevantes dos usuários.

# 2) Composição: agrupar dados e subrotinas e ocultar dados irrelevantes dos usuários.

# 3) Dunders: __dunders__ - Métodos especiais

# 4) super(): função de chamar o método definido na super classe

class Passaro:
    def __int__(self, nome):
        self.nome = nome

class CanarinhoPistola(Passaro):
    def __int__(self, nome, camisa):
        super().__int__(nome)
        self.camisa = camisa


# 5) __new__, __init__, __del__:

class MinhaClasse:
    def __new__(cls):
        print("Construindo")
        return super().__new__(cls)
    def __int__(self):
        print("Inicializando")
    def __del__(self):
        print("Finalizando")

a = MinhaClasse()
print(a)
del a
# print(a)

# 6) __str__:

class Passaro:
    def __init__(self, nome):
        self.nome = nome

class CanarinhoPistola(Passaro):
    def __init__(self, nome, camisa):
        super().__init__(nome)
        self.camisa = camisa

    def __str__(self):
        return f"CanarinhoPistola(nome='{self.nome}', camisa='{self.camisa}')"

canarinhoPistola = CanarinhoPistola("Pistola", 10)
print(canarinhoPistola.nome)
print(canarinhoPistola.camisa)
print(canarinhoPistola)