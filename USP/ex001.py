segundos=int(input('informe o número em segundos que deseja converter: '))

horas = segundos // 3600
segundosRestantes = segundos % 3600
minutos = segundos // 60
segundosRestantesFinal = segundos % 60

print('Horas {}, minutos {} e segundos {}'.format(horas, minutos, segundosRestantesFinal))
