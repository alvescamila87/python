class Cliente:
    def __int__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:

    def __int__(self, clientes, numero, saldo=0):
        self.saldo = saldo
        self.numero = numero
        self.clientes = clientes
    def resumo(self):
        print('CC Número: %s Saldo: %10.2f' % (self.numero, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
    def deposito(self, valor):
        self.saldo += valor


camila = Cliente()
camila.nome = "Camila"
camila.telefone = '79651-56161'
print(camila.nome, camila.telefone)