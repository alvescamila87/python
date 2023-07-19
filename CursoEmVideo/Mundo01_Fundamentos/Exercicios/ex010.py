carteira=float(input('quanto dinheiro você possui na carteira? R$:'))
dolar=6.00
euro=7.00
conversorDolar=carteira/dolar
conversorEuro=carteira/euro
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(carteira, conversorDolar))
print('Com R${:.2f} você pode comprar US${:.2f}.'.format(carteira, conversorEuro))