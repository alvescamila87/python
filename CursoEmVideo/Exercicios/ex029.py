velocidade=int(input('Qual a velicidade atual do carro? '))
multa=velocidade
if velocidade <= 80:
    print('Dirija com segurança!')
else:
    multa=(velocidade-80)*7
    print('MULTADO! Você foi excedeu o limite permitido de {}km/h. Multa a pagar R$ {:.2f}!'.format(velocidade, multa))
