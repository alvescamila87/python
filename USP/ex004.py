n = int(input("Digite o tam da seq: ")) # atribuição multipla

conta_par = 0
cont = 0
while cont < n:
    num = int(input("Digite um num da seq: "))
    cont = cont + 1
    if num % 2 == 0:  # se num é múltiplo de 2, ou seja, é par
        conta_par = conta_par + 1

print(conta_par,   "numeros pares")
print(n - conta_par, "numeros impares")