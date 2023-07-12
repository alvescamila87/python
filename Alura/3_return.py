def velocidade(espaco, tempo):
    v = espaco / tempo
    return v

print(velocidade(100,20))

#opção 2: atribuir a uma variavel
resultado = velocidade(100,20)
print(resultado)


#opção 3: utilizar no cálculo de aceleração
aceleracao = velocidade(100,20)/20
print(aceleracao)

#retorno de string
def dados(idade=None):
    if idade is not None:
        return "Idade: {} anos".format(idade)
    else:
        return "Idade não informada"
    
#retorno de dicionario + laço for
def calculadora(x, y):
    return {'soma':x + y, 'subtração':x-y}

resultados = calculadora(1,2)
for key in resultados:
    print('{}: {}'.format(key, resultados[key]))
