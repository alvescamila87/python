carteira=float(input('quanto dinheiro você possui na carteira? R$:'))
dolar=3.27
conversorDolar=carteira/dolar
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(carteira, conversorDolar))