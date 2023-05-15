#Dados números inteiros n, i e j, todos maiores do que zero, imprimir em ordem crescente os n primeiros naturais que são múltiplos de i ou de j e ou de ambos.
#Por exemplo, para n = 6, i = 2 e j = 3 a saída deverá ser:
#0   2   3   4   6   8

n = int(input('informe o valor "n": '))
i = int(input('informe o valor "i": '))
j = int(input('informe o valor "j": '))

multiplo = 0
k = 0

while k < n:
    if multiplo % i == 0 or multiplo % j == 0:
        print(multiplo)
        k = k + 1

    multiplo = multiplo + 1
