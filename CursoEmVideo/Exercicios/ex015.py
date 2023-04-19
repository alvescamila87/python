diarias=int(input('Quantos dias alugados?'))
kmRodados=float(input('Quantos km rodados?'))
carro=60
km=0.15
total=(kmRodados*km)+(diarias*carro)
print('O total a pagar é de R${:.2f}.'.format(total))

