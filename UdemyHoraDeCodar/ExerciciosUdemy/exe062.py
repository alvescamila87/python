#orientação objeto: exercicio banco

class Banco:
    def __init__(self, proprietario, saldo):
        self.proprietario = proprietario
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor
        print("Depósito de: R$%.2f. Saldo atualizado R$%.2f." %(valor, self.saldo))

    def sacar(self, valor):
        self.saldo = self.saldo - valor
        print("Saque de: R$%.2f. Saldo atualizado R$%.2f." %(valor, self.saldo))

    def transferir(self, outra_conta, valor):
        self.saldo = self.saldo - valor
        outra_conta.saldo = outra_conta.saldo + valor
        print("Transferência de: R$%.2f para outra conta. Saldo atualizado R$%.2f." %(valor, self.saldo))
        
#iniciar conta camila
conta_1 = Banco("Camila", 1000)
print(conta_1.saldo)

conta_1.sacar(500)
print(conta_1.saldo)

#iniciar conta maria
conta_2 = Banco("Maria", 50)
print(conta_2.saldo)

#transferir de camila para maria
conta_1.transferir(conta_2, 200)
print(conta_2.saldo)

#verificar saldo da conta camila
print(conta_1.saldo)

#deposito para camila
conta_1.depositar(55)
print(conta_1.saldo)