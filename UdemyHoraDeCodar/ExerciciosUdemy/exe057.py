#funcao com sequencia de paramtros

def mutiplica_numeros(*nums):
    multiplicacao = 1 #colocar '1', senão sempre multiplicará por 'zero'
    for num in nums:
        multiplicacao *= num

    return multiplicacao

multiplicacao_1 = mutiplica_numeros(2, 2, 10, 6, 9)
print(multiplicacao_1)