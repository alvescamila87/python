#estrutura de repetição: exercício soma de ímpares múltiplos de três

s = 0
contador = 0
for impar in range(1,501,2):
    if impar % 3 == 0:
        print(impar, end=" ")
        contador += 1
        s += impar
print("A soma de {} números ímpares solicitados e que são múltiplos de 3 é de: {}".format(contador, s))
