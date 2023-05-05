segundos=int(input('Por favor, entre com o número de segundos que deseja converter: '))
a = segundos // 86400
segundos_rest = segundos % 86400
b = segundos_rest // 3600
segundos_rest = segundos_rest % 3600
c = segundos_rest // 60
d = segundos_rest % 60
print('{} dias, {} horas, {} minutos e {} segundos.'.format(a, b, c, d))

#forma de cálculo
#O operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor. O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.
#pega o total de segundos e divide por 86400 (a quantidade de segundos em um dia), o resultado (descontando as casas decimais) é o total de dias
#pega o resto da divisão por 86400, assim tem-se a "sobra" (a quantidade de segundos que não é suficiente para completar um dia)
#depois divide esse resultado por 3600 (a quantidade de segundos em uma hora), o resultado (descontando as casas decimais) é o total de horas
#pega o resto da divisão por 3600, assim tem-se a "sobra" (a quantidade de segundos que não é suficiente para completar uma hora)
#depois divide esse resultado por 60 (a quantidade de segundos em um minuto), o resultado (descontando as casas decimais) é o total de minutos
#pega o resto da divisão por 60, assim tem-se a "sobra" (a quantidade de segundos que não é suficiente para completar um minuto)