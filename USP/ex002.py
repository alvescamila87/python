import math

#fazer programa que calcule as raízes de 2º
#equação quadrática
#calcular apenas raízes reais
#se delta menor que zero, 'essa equação não possui raizes reais {}'
#se delta for igual a zero, 'essa equação possui raizes reais {}'
#se delta for maior a zero, 'as raízes dessa equação são: 1ª raiz: {} e 2ª raiz: {}'
#ax2 + bx + c = 0

math.sqrt(8)
print()

a = int(input('Informe o valor de a:'))
b = int(input('Informe o valor de b: '))
c = int(input('Informa o valor de c:' ))

delta = (b ** 2) - 4 * a * c

if a == 0:
    print('Essa equação não possui raizes reais {}'.format(delta))
if delta < 0:
    print('Essa equação possui raizes reais.')
else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)
    
    print('As raízes dessa equação são: 1ª raiz: {} e 2ª raiz: {}'.format(x1, x2))

