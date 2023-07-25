#estrutura de repetição: maior e menor valores

continuar = "S"
contador = 0
media = 0
menor_valor = 0
maior_valor = 0
soma = 0

while continuar not in "Nn":
    num = int(input("Digite um número: "))
    continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    soma += num
    contador += 1
    if contador == 1:
        maior_valor = num
        menor_valor = num
    else:
        if num > maior_valor:
            maior_valor = num
        if num < menor_valor:
            menor_valor = num

media = soma / contador
print("Você digitou {} números e a média foi de {}.".format(contador, media))
print("O maior valor foi {} e o menor valor foi {}.".format(maior_valor, menor_valor))



