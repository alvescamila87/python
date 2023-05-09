#Dados um número inteiro n, n > 0, e uma sequência com n números inteiros, determinar quantos números da sequência são pares e quantos são ímpares. Por exemplo, para a sequência
#6   -2   7   0  -5   8  4
# o seu programa deve escrever o número 4 para o número de pares e 2 para o de ímpares.
# Solução 1: Essa é uma solução comum que usa if-else.


n = int(input('digite tamanho da sequência de números: '))

contagem = contagem_par = contagem_impar = 0
while contagem < n:
    num = int(input('informe um número da sequência: '))
    contagem = contagem + 1
    if num % 2 == 0: # se num é múltiplo de 2, ou seja, é par
        contagem_par = contagem_par + 1
    else:
        contagem_impar = contagem_impar + 1

print(contagem_par, "números pares")
print(contagem_impar, "números ímpares")

