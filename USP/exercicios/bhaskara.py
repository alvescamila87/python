import math

a=float(input('Informe o valor de a: '))
b=float(input('Informe o valor de b: '))
c=float(input('Informe o valor de c: '))
delta = (b ** 2) - 4 * a * c

if delta == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print('a raiz dupla desta equação é {}'.format(raiz1))
else:
    if delta < 0:
        print('esta equação não possui raízes reais')
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        if raiz1 < raiz2:
            print('as raízes da equação são {} e {} '.format(raiz1, raiz2))
        else:
            print('as raízes da equação são {} e {} '.format(raiz2, raiz1))


