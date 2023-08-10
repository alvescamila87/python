#Estruturas compostas: Dicionários {} - EXERCÍCIO: Aprimorando dicionários

time = list()
jogador = dict()

while True:
    jogador['nome'] = str(input("Nome do jogador: ")).strip().capitalize()
    jogador['partidas'] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    jogador['gols'] = lista_gols = []
    for p in range(0, jogador['partidas']):
          lista_gols.append(int(input(f"Quantos gols na partida {p}? ")))
    jogador['total gols'] = sum(lista_gols)
    time.append(jogador.copy())
    while True:
          continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
          if continuar in "SN":
               break
          print("ERRO! Digite apenas S ou N.")
    if continuar == "N":
         break
    
print("DICIONÁRIO: ", jogador)
print("LISTA: ", time)
        
# Lista de jogadores:
print("-="*30)
print(f"{'cod':>2}{'nome':<4}{'gols':<10}{'total gols':>8}")
print("-"*30)
for jogador in time:
     for k, v in jogador.items():
          print(f'{k} = {v}')
print("-="*30)

# Mostrar dados individualmente de jogador:
while True:
     print('-'*30)
     opcao = int(input("Mostrar dados de qual jogador? (999 para parar) "))
     if opcao == 999:
          print("FINALIZANDO...")
          break
     if opcao <= len(time) - 1:
          print(f" -- LEVANTAMENTO DO JOGADOR {jogador[opcao][0]}:")
          for k, v in enumerate(lista_gols):
               print(f"No jogo {k} fez {v} gols.")

