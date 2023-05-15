#Leitura e soma de uma sequência
#Dada uma sequência de números inteiros diferentes de zero, terminada por um zero, calcular a sua soma

num = int(input('informe1 um número ou zero para terminar: '))
soma = 0

while num != 0:
    soma = soma + num
    num = int(input('informe2 um número ou zero para terminar: '))

print('A soma foi: ', soma)