#estrutura de repetição: exercício soma de ímpares múltiplos de três

soma = 0
contador = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        print(impar, end=" ")
        contador += 1
        soma += impar
print("A soma de {} números ímpares solicitados e que são múltiplos de 3 é de: {}".format(contador, soma))
