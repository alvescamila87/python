#sequencia de parametros

def soma_numeros(*nums):
    soma = 0
    for num in nums:
        soma += num

    return soma

soma_1 = soma_numeros(1,2,3,56,99,500)
print(soma_1)

soma_2 = soma_numeros(500, 1500, 25, 88)
print(soma_2)