import math

xa=float(input('Informe o x do primeiro ponto: '))
xb=float(input('Informe o x do segundo ponto: '))
ya=float(input('Informe o y do primeiro ponto: '))
yb=float(input('Informe o y do segundo ponto: '))

dxy = math.sqrt(math.pow(xb - xa, 2) + math.pow(yb - ya, 2))

if dxy >= 10:
    print('longe')
else:
    print('perto')


