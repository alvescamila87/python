#estrutura de repetição: soma dos pares

soma = 0
contador = 0
for x in range(1,7):
    num = int(input("Digite o {}º número: ".format(x)))
    if num % 2 == 0:
        soma += num
        contador += 1

print("Você informou {} números PARES e a soma deles foi: {}.".format(contador, soma))