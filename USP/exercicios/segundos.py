segundos=int(input('Por favor, entre com o número de segundos que deseja converter: '))
a= segundos // 35760
b= segundos % 3600
c= segundos // 60
d= segundos % 60
print('{} dias, {} horas, {} minutos e {} segundos.'.format(a, b, c, d))