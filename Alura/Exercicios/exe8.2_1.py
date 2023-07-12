#criando uma conta

def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    conta['saldo'] = conta['saldo'] + valor

def saca(conta, valor):
    conta['saldo'] = conta['saldo'] - valor

def extrato(conta):
    print('conta: {}, saldo atualizado: {}, limite: {}'. format(conta['numero'], conta['saldo'], conta['limite']))

conta = cria_conta(663281-8, "Camila", 10000, 50000)
extrato(conta)
deposita(conta, 6666)
extrato(conta)