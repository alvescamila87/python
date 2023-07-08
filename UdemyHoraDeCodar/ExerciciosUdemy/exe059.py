#funcao random randint

from random import randint
from time import sleep

def gera_numero():
    computador = randint(1,10) #faz o pc sortear um número
    jogador = int(input("Tente advinhar o número a ser sorteado de 1 a 10: "))
    print("PROCESSANDO...")
    sleep(2) #faz "suspense" de tempo para o processamento
    if jogador == computador:
        print("Você acertou!!! Você informou %d e o sorteado foi %d." %(jogador, computador))
    else:
        print("Você NÃO acertou... :( você informou %d e o sorteado foi %d." %(jogador, computador))

gera_numero()
