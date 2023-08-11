#estruturas compostas: tuplas com times de futebol

times_brasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR', 
                     'São Paulo', 'Fluminense', 'Red Bull Bragantino', 'Fortaleza', 
                     'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos', 
                     'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG',
                     'Vasco da Gama')

# Lista do Brasileirão:
print("-=-"*20)
print(f"Lista de time dos Brasileirão 2023: {times_brasileirao}")

# Os 5 primeiros da lista:
print("-=-"*20)
print(f"Os 5 primeiros times de 2023 são: {times_brasileirao[0:5]}")

# Os 4 primeiros da lista:
print("-=-"*20)
print(len(times_brasileirao))
print(f"Os 4 últimos times de 2023 são: {times_brasileirao[16:]}")
print(f"Os 4 últimos times de 2023 são: {times_brasileirao[-4:]}")

# Posição do Corinthians em 2023:
print("-=-"*20)
print(f"O Corinthians está na {times_brasileirao.index('Corinthians')+1}ª posição do Brasileirão 2023.")

# A lista em ordem alfabética:
print("-=-"*20)
print(f"A lista dos times do Brasileirão de 2023 em Ordem Alfabética: {sorted(times_brasileirao)}")
print("-=-"*20)