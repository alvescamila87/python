from random import randint
from time import sleep
computador = randint(0,5) #Faz o PC sortear
print('-'*80)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-'*80)
jogador=int(input('Em que número pensei? ')) #Jogador tenta informar o número a ser sorteado/pensado pelo PC
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou o número')
else:
    print('Você NÃO acertou, pois eu pensei no número {} e não no {}.'.format(computador, jogador))
