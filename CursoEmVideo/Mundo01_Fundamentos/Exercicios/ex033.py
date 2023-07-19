n1 = int(input('digite um número: '))
n2 = int(input('digite um segundo número: '))
n3 = int(input('digite um terceiro número: '))
# verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# verificar quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor número é o {} e o maior valor é o {}'.format(menor, maior))
