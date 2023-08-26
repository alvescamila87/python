# OOP: Herança e Polimorfismo

# 1)  Herança:
class Pizza:
    pecados = 8

    @classmethod # Escopo compartilhado
    def mudar_tamanho(cls, pedacos):
        cls.pedaco = pedacos

class FrangoCatupiry(Pizza):
    pass

class Pepperoni(Pizza):
    pass

class BananaNevada(Pizza):
    pass

# Herança múltipla
class MeioAMeio(FrangoCatupiry, Pepperoni):
    pass

# 2)  Polimorfismo: (sobrescrever / overwriting) para reuso de software

class Pizza:
    pecados = 8

    @classmethod # Escopo compartilhado
    def mudar_tamanho(cls, pedacos):
        cls.pedaco = pedacos

    @staticmethod
    def ingredientes():
        return "Ingredientes"

class FrangoCatupiry(Pizza):
    @staticmethod
    def ingredientes():
        return ['queijo',
                'catupiry',
                'frango']

print(Pizza.ingredientes)
print(Pizza.ingredientes()) # herdou pizza
print(FrangoCatupiry.ingredientes()) # herdou pizza, mas sobrescreveu ingredientes