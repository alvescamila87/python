n1=float(input('digite sua primeira nota: '))
n2=float(input(('digite sua segunda nota: ')))
m=(n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=7:
    print('Parabéns!!!')
else:
    print('Estude mais...')
#print('Parabéns' if m>=7 else 'Estude mais...') //condição simplificada