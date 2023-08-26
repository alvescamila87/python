# OOP: Diferença entre CLS e SELF, Herança e Polimorfismo

# 1)  Diferença entre CLS e SELF - Exemplo 1
class Fila:
    """Abstração de qualquer tipo de Fila:
        - supermercado
        - processos
        - ...
    """

    # (CLS) Compartilhado
    # Escopo compartilhado
    c_fila = []

    @classmethod
    def c_entrar(cls, objeto):
        cls.c_fila.append(objeto)
        print(cls.c_fila)

    # (Self) Específico
    # Escopo Específico
    def __int__(self):
        self.s_fila = []

    def s_entrar(self, objeto):
        self.s_fila.append(objeto)
        print(self.s_fila)

banco = Fila()
supermercado = Fila()
processos = Fila()
banco.c_fila
banco.c_entrar("Guilherme") # Escopo compartilhado
banco.c_fila # Escopo compartilhado
supermercado.c_fila # Escopo compartilhado
processos.c_fila # Escopo compartilhado


banco.s_entrar("João") # Escopo específico
supermercado.s_entrar("Camila") # Escopo específico
banco.s_fila # Escopo específico
supermercado.s_fila # Escopo específico
processos.s_fila # Escopo específico



# 1)  Diferença entre CLS e SELF - Exemplo 2

class Pizza:
    pecados = 8

    def __int__(self, sabor):
        self.sabor = sabor

    def pegar_pedaco(self): # Escopo específico
        "Método de instância"
        self.pecados -= 1

    @classmethod # Escopo compartilhado
    def mudar_tamanho(cls, pedacos):
        cls.pedaco = pedacos

    @staticmethod
    def ingredientes(): # Método / Função aleatória que independe dos demais
        return "Molho de tomate, queijo e cebola"