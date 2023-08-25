# INTRO OOP

class Fila:
    def __init__(self):
        self.fila = []
    def entrar(self, nome):
        self.fila.append(nome)

    def sair(self):
        self.fila.pop(0)

supermercado = Fila()

supermercado.entrar("Camila")
supermercado.entrar("Karoline")
supermercado.entrar("Isabel")
print(supermercado.fila)
supermercado.sair()
supermercado.sair()
supermercado.sair()
print(supermercado.fila)