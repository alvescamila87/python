from math import sin, cos, tan, radians
a=float(input('digite o ângulo que você deseja:'))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O ângulo {} possui o SENO de {:.2f}'.format(a, s))
print('O ângulo {} possui o COSSENO de {:.2f}'.format(a, c))
print('O ângulo {} possui o TANGENTE de {:.2f}'.format(a, t))