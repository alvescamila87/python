#programação orientada a objetos: histórico da conta

import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print("Data abertura: {}" .format (self.data_abertura))
        print("Transações: ")
        for t in self.transacoes:
            print("-", t)

class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf= cpf

class Conta:
    def __init__(self, numero, cliente, saldo, limite=7000):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.limite = limite
        #recebe a classe histórico, a existência do histórico depende da existência da conta
        self.historico = Historico()

    def depositar(self, valor):
        self.saldo += valor
        self.historico.transacoes.append("Depósito de R${:.2f}" .format(valor))
        print("Depósito de R${:.2f} realizado com sucesso! Saldo atualizado R${:.2f}." %(valor, self.saldo))

    def sacar(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("Saque de R${:.2f}" .format(valor))
            print("Saque de R$%.2f realizado com sucesso! Saldo atualizado R${:.2f}." %(valor, self.saldo))
    
    def extrato(self):
        print("Conta: {} - Saldo atualizado: R${:.2f}, Limite: {:.2f}" .format(self.numero, self.saldo, self.limite))
        self.historico.transacoes.append("Imprimindo extrato - Saldo de R$ {:.2f}" .format(self.saldo))

    def transferir_para(self, destino, valor):
        retirou = self.sacar(valor)
        if (retirou == False):
            return False
        else:
            destino.depositar(valor)
            self.historico.transacoes.append("Transferência de R${:.2f} para a conta {}" .format(valor, destino.numero))
            return True


cliente1 = Cliente("Isabel", "Oliveira", "111111111-11")
cliente2 = Cliente("Paulo", "José", "222222222-22")

conta1 = Conta("1234-5", cliente1, 17000)
conta2 = Conta("9632-7", cliente2, 16900)

conta1.depositar(500)
conta1.sacar(150)
conta1.transferir_para(conta2, 666)
conta1.extrato()

conta1.historico.imprimir()
conta2.historico.imprimir()

#metodos:
print(dir(Conta))
print(vars(conta1))