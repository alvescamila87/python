#programação orientada a objetos: método transfere

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def extrato(self):
        print("A conta: {} Titular: {}. Saldo atualizado: R${}, Limite: {}" .format(self.numero, self.titular, self.saldo, self.limite))

    def transferir_para(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor
        print("Transferência de: R$%.2f para outra conta. Saldo atualizado R$%.2f." %(valor, self.saldo))


conta1 = Conta("123-4", "Camila", 10000, 50000)
conta1.extrato()
    
conta1.depositar(500)
conta1.extrato()

conta1.sacar(200)
conta1.extrato()

conta2 = Conta("999-5", "Isabel", 30000, 75000)
conta2.extrato()

conta1.transferir_para(conta2, 3333)
conta1.extrato()
conta2.extrato()