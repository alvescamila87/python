#analisando triângulos v2

lado1 = float(input("Informe tamanho do 'LADO 1': "))
lado2 = float(input("Informe tamanho do 'LADO 2': "))
lado3 = float(input("Informe tamanho do 'LADO 3': "))
if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
    print('Formou um triângulo!', end='')
    if lado1 == lado2 == lado3:
        print("Triângulo EQUILÁTERO: todos os lados iguais: {}, {}, {},".format(lado1, lado2, lado3))
    elif lado1 != lado2 != lado3 != lado1:
        print("Triângulo ESCALENO: todos os lados diferentes: {}, {}, {},".format(lado1, lado2, lado3))
    else:
        print("Triângulo ISÓSCELES: dois lados iguais: {}, {}, {},".format(lado1, lado2, lado3))
else:
    print('NÃO formou um triângulo!')