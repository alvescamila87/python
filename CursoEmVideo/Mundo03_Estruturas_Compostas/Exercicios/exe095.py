#Estruturas compostas: Dicionários {} - EXERCÍCIO: Aprimorando dicionários

#OPÇÃO CAMILA
time = list()
jogador = dict()

while True:
    jogador['nome'] = str(input("Nome do jogador: ")).strip().capitalize()
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador['gols'] = lista_gols = []
    for p in range(0, jogador['partidas']):
          lista_gols.append(int(input(f"Quantos gols na partida {p+1}? ")))
    jogador['total gols'] = sum(lista_gols)
    time.append(jogador.copy())
    while True:
          continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
          if continuar in "SN":
               break
          print("ERRO! Digite apenas S ou N.")
    if continuar == "N":
         break
        
# Lista de jogadores:
# Utilizar enumerate visto que 'time' é uma lista
print("-="*30)
print(f"cod ", end="")
for i in jogador.keys():
     print(f"{i:<15}", end="")
print()
print('-'*40)
for k, v in enumerate(time):
     print(f'{k:>3} ', end="")
     for d in v.values():
          print(f"{str(d):15}", end="")
     print()
print("-="*30)

# Mostrar dados individualmente de jogador:
while True:
     print('-'*30)
     opcao = int(input("Mostrar dados de qual jogador? (999 para parar) "))
     if opcao == 999:
          print("FINALIZANDO...")
          break
     if opcao >= len(time):
          print(f"ERRO! Não existe jogador com esse código '{opcao}'!")     
     else:
          print(f" -- LEVANTAMENTO DO JOGADOR {time[opcao]['nome']}:")
          for k, v in enumerate(time[opcao['gols']]):
               print(f"    No jogo {k+1} fez {v} gols.")
     print('-'*40)
print('<< VOLTE SEMPRE >>')

#OPÇÃO GUANABARA

time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input("Nome do jogador: "))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for p in range(0, tot):
          partidas.append(int(input(f"Quantos gols na partida {p+1}? ")))
    jogador['gols'] = partidas[:]
    jogador['total gols'] = sum(partidas)
    time.append(jogador.copy())
    while True:
          resp = str(input("Quer continuar? [S/N] ")).upper()[0]
          if resp in "SN":
               break
          print("ERRO! Digite apenas S ou N.")
    if resp == "N":
         break
        
# Lista de jogadores:
# Utilizar enumerate visto que 'time' é uma lista
print("-="*30)
print(f"cod ", end="")
for i in jogador.keys():
     print(f"{i:<15}", end="")
print()
print('-'*40)
for k, v in enumerate(time):
     print(f'{k:>3} ', end="")
     for d in v.values():
          print(f"{str(d):15}", end="")
     print()
print("-="*30)

# Mostrar dados individualmente de jogador:
while True:
     print('-'*30)
     busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
     if busca == 999:
          print("FINALIZANDO...")
          break
     if busca >= len(time):
          print(f"ERRO! Não existe jogador com esse código '{busca}'!")     
     else:
          print(f" -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}:")
          for i, g in enumerate(time[busca]['gols']):
               print(f"    No jogo {i+1} fez {g} gols.")
     print('-'*40)
print('<< VOLTE SEMPRE >>')