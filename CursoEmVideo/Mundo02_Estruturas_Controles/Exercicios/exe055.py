#estrutura de repetição: maior e menor sequência de peso

maior_peso = 0
menor_peso = 0

for pessoa in range(1,6):
    peso = float(input("Digite o peso da {}ª pessoa: ".format(pessoa)))
    if pessoa == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
            

print("O maior peso lido foi de {:.2f}kg.".format(maior_peso))
print("O maior peso lido foi de {:.2f}kg.".format(menor_peso))