#Estruturas compostas: Dicionários {} - EXERCÍCIO: Cadastro de Jogador de Futebol

# Opção Camila
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


# Opção Guanabara:

jogador2 = dict()
partidas = list()

jogador2["nome"] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador2['nome']} jogou? "))
for c in range(0, total):
     partidas.append(int(input(f"    Quantos gols na partida {c}? ")))
jogador2["gols"] = partidas[:]
jogador2['total'] = sum(partidas)
print("-="*30)
print(jogador2)
print("-="*30)
for k, v in jogador2.items():
     print(f"O campo {k} tem o valor {v}")
print("-="*30)
print(f"O jogador {jogador2['nome']} jogou {len(jogador2['gols'])} partidas.")
for i, v in enumerate(jogador2['gols']):
     print(f"    => Na partida {i}, fez {v} gols.")
print(f"Foi um total de {jogador2['total']} gols")