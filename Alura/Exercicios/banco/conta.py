import datetime

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        
class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print("Data da abertura: {}" .format(self.data_abertura))
        print("Transções: ")
        for t in self.transacoes:
            print("-", t)

class Conta:
    def __init__(self, numero, cliente, saldo, limite):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de R$ {}".format(valor))
        print("Depósito de R${}" .format(valor))

    def sacar(self, valor):
        if self.saldo < valor:
            print("Você não possui saldo suficiente para realizar o saque")
            return False
        else:
            self.saldo -= valor
            print("Saque de R${}" .format(valor))

    def extrato(self):
        self.historico.transacoes.append("Tirou extrato")
        print("Extrato da conta - Conta: {} Titular: {} Saldo: R$ {}" .format(self.numero, self.titular, self.saldo))

    # Esse	método	deve	sacar	o	valor	do	próprio	objeto	e depositar	na	conta	destino
    def transferir_para(self, outra_conta, valor):
        retirou = self.sacar(valor)
        if retirou == False:
            return False
        else:
            outra_conta.depositar(valor)
            return True


