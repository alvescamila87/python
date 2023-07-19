distancia = int(input('Qual a distância da viagem? '))
if distancia <= 200:
    print('Viagem padrão. A sua viagem é de {}km e o preço é de R${:.2f}'.format(distancia, distancia * 0.50))
else:
    print('Viagem longa. A viagem é de {}km e o preço é de R${:.2f}'.format(distancia, distancia * 0.45))
