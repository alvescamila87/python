#Estruturas compostas: Dicionários {} - EXERCÍCIO: Jogo de dados em python

from random import randint
from time import sleep
# from operator import itemgetter --> DEPRECATED

# Para sortear as jogadas no dado
jogos_dado = {
              'jogador1': randint(1,6),
              'jogador2': randint(1,6),
              'jogador3': randint(1,6),
              'jogador4': randint(1,6)
              }

# Para colocar na ordem
ranking = dict()

print('Valores sorterados:')

# Para mostrar o que cada jogador tirou no dado
for k, v in jogos_dado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

# Para colocar em ordem por parte de valor(1), caso contrário seria chave(0)
# ranking = sorted(jogos_dado.items(), key=itemgetter(1), reverse=True) --> DEPRECATED
ranking = sorted(jogos_dado.items(), key=lambda item: item[1], reverse=True)
print("-="*30)
print('  == RANKING DOS JOGADORES ==')

# Tratar resultado como lista
for i, v in enumerate(ranking):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)