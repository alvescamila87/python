#JOKENPO: Game pedra, papel, teroura

from random import randint
from time import sleep

print('{:=^40}'.format(' GAME: PEDRA, PAPEL, TESOURA '))
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

itens = ('Pedra', 'Papel', 'Tesoura')

computador = randint(0,2) #Faz PC sortear jogada

jogador = int(input("Escolha a sua jogada: "))



print("PROCESSANDO...")
sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(1)

print('-=' * 10)

print("PC jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))

print('-=' * 10)

if computador == 0: #PC jogou PEDRA
    if jogador == 0:
        print("Empate!")
    elif jogador == 1:
        print("Jogador venceu!")
    elif jogador == 2:
        print("PC venceu!")
    else:
        print("Jogada inválida!!!")
elif computador == 1: #PC jogou PAPEL
    if jogador == 0:
        print("PC venceu!")
    elif jogador == 1:
        print("Empate!")
    elif jogador == 2:
        print("Jogador venceu!")
    else:
        print("Jogada inválida!!!")
elif computador == 2: #PC jogou TESOURA
    if jogador == 0:
        print("Jogador venceu!")
    elif jogador == 1:
        print("PC venceu!")
    elif jogador == 2:
        print("Empate!")
    else:
        print("Jogada inválida!!!")

