#programação orientada a objetos: métodos

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        #print('Inicializando uma conta')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo = self.saldo + valor

    def saca(self, valor):
        self.saldo = self.saldo - valor

    def extrato(self):
        print('número: {}, saldo atualizado: {}' .format(self.numero, self.saldo))

    def transfere_para(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor
               


#instanciar objeto 
conta = Conta('123-4', "Camila", 1000, 5000)

#manipular objeto e acessar atributos
print(conta.titular)
print(conta.saldo)

#chamar o método deposita
conta.deposita(200)
print(conta.saldo)

conta.saca(50)
print(conta.saldo)

conta.extrato()

#charmar o método transfere para

conta2 = Conta('999-5', "Isabel", 100, 50000)

# conta.transfere_para("999-5", 50)
# print(conta.saldo)