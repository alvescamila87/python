num=int(input('Digite um número: '))

cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        cont = cont + 1

if cont == 2:
    print('primo')
else:
    print('não primo')