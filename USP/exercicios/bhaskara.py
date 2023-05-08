import math

a=float(input('Informe o valor de a: '))
b=float(input('Informe o valor de b: '))
c=float(input('Informe o valor de c: '))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print('esta equação não possui raízes reais')
else:
    if delta < 0:
        print('a raiz desta equação é {}'.format(delta))
    else:
        if delta == 0:
            x0 = - b / (2 * a)
            print('delta menor que 0,  raiz = {}'.format(x0))
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

            print('raízes: x1 = {} x2 = {}'.format(x1, x2))


