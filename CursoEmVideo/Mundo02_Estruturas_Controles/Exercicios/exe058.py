#estrutura de repetição: jogo de advinhação v2
    
from random import randint
computador = randint(0,10) #Faz o PC sortear
print('-'*80)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue advinhar qual foi?')
print('-'*80)
jogador=int(input('Qual é o seu palpite? ')) #Jogador tenta informar o número a ser sorteado/pensado pelo PC
tentativas = 0
acertou = False
while not acertou:
    jogador=int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... tente novamente!")
        else:
            print("Menos... tente novamente!")

print("Acertou!!! Foram {} tentativas para acertar" .format(tentativas))
