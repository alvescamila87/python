#programação orientada a objetaos

def criar_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] = conta['saldo'] + valor

def saca(conta, valor):
    conta['saldo'] = conta['saldo'] - valor

def extrato(conta):
    print('numero: {}, saldo: {}'.format(conta['numero'], conta['saldo']))

conta_1 = criar_conta('123-4', 'Camila', 200.00, 1.000)

#visualizar dados
print(conta_1)

#visualizar dados por chave
print(conta_1['numero'])

deposita(conta_1, 313.13)
extrato(conta_1)
saca(conta_1, 50.00)
extrato(conta_1)
