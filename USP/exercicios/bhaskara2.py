import math

#função delta
def delta(a, b, c):
    return (b ** 2) - 4 * a * c

#função da entrada de dados
def main():
    a=float(input('Informe o valor de a: '))
    b=float(input('Informe o valor de b: '))
    c=float(input('Informe o valor de c: '))
    imprime_raizes(a, b, c)

#função imprime raízes
def imprime_raizes(a, b, c):
    #chamar uma única vez e guardar numa variável 'd' (delta)
    d = delta(a, b, c)
    if d == 0:
        raiz1 = (-b + math.sqrt(d)) / (2 * a)
        print('a raiz dupla desta equação é {}'.format(raiz1))
    else:
        if d < 0:
            print('esta equação não possui raízes reais')
        else:
            raiz1 = (-b + math.sqrt(d)) / (2 * a)
            raiz2 = (-b - math.sqrt(d)) / (2 * a)
            print('as raízes da equação são {} e {} '.format(raiz1, raiz2))

