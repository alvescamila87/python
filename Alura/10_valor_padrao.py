#programação orientada a objetos: atributos de classe ou argumentos de função podem receber valor padrão

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

    def depositar(self, valor):
        self.saldo += valor
        print("Depósito de R$%.2f realizado com sucesso! Saldo atualizado R$%.2f." %(valor, self.saldo))

    def sacar(self, valor):
        self.saldo -= valor
        print("Saque de R$%.2f realizado com sucesso! Saldo atualizado R$%.2f." %(valor, self.saldo))

    def transferir_para(self, destino, valor):
        self.saldo -= valor
        destino.saldo += valor
        print("Transferência de: R$%.2f para outra conta. Saldo atualizado R$%.2f." %(valor, self.saldo))

    def extrato(self):
        print("Extrato da conta: {} e Titular: {}. Saldo atualizado: R${}, Limite: {}" .format(self.numero, self.titular, self.saldo, self.limite))


#Instanciar objeto de cliente
cliente1 = Cliente("Camila", "Cabral", "1111111111-1")
print(cliente1.nome, cliente1.cpf)

#Instanciar objeto conta e passar o cliente como titular da conta
conta1 = Conta("12345-6", cliente1, 5000)
conta1.extrato()

#Acessar a referência 'Cliente' da conta 
print(conta1.titular)

#Acessar o atributo do objeto referência 'Cliente'
print(conta1.titular.nome)


#Tipo
print(type(conta1.numero))
print(type(conta1.saldo))
print(type(conta1.limite))