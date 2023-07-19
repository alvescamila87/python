r1 = float(input('Informe tamanho do retângulo 1: '))
r2 = float(input('Informe tamanho do retângulo 2: '))
r3 = float(input('Informe tamanho do retângulo 3: '))
if r1<r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formou um triângulo!')
else:
    print('NÃO formou um triângulo!')