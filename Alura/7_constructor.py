#programação orientada a objetos: constructor

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print('Inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


#instanciar objeto 
conta = Conta(123-4, "Camila", 1000, 5000)

#manipular objeto e acessar atributos
print(conta.titular)
print(conta.saldo)