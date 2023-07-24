#estrutura de repetição:cálculo de fatorial

numero = int(input("Digite um número para calcular seu Fatorial: "))
f = 1
for x in range(1,numero + 1):
    f *= x

print("O fatorial de {}! é {}".format(numero, f))
