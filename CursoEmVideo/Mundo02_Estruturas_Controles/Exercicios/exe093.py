#Estruturas compostas: Dicionários {} - EXERCÍCIO: Cadastro de Jogador de Futebol

jogador = dict()


jogador["nome"] = str(input("Nome do jogador: "))
jogador["partidas"] = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
jogador["gols"] = lista_gols = []
for n in range(0, jogador["partidas"]):
    lista_gols.append(int(input(f"    Quantos gols na partida {n}? ")))
# Print 1
print("-="*30)
print(jogador)
print("-="*30)
# Print 2
jogador["total gols"] = sum(lista_gols)
for k, v in jogador.items():
    print(f" - O campo '{k}' tem o valor '{v}'.")
print("-="*30)
# Print 3
print(f"O jogador {jogador['nome']} jogou {jogador['partidas']} partidas.")
for chave, n in enumerate(lista_gols):
        print(f"Na posição {chave}, o número '{n}' foi adicionado.")
print(f"Foi um total de {jogador['total gols']} gols marcados.")
