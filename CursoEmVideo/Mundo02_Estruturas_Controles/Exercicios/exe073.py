#estruturas compostas: tuplas com times de futebol

times_brasileirao = ('Botafogo', 'Grêmio', 'Flamengo', 'Palmeiras', 'Athletico-PR', 'São Paulo', 'Fluminense', 'Red Bull Bragantino', 'Fortaleza', 'Internacional', 'Cruzeiro', 'Cuiabá', 'Atlético-MG', 'Santos', 'Corinthians', 'Goiás', 'Bahia', 'Coritiba', 'América-MG','Vasco da Gama')

print(len(times_brasileirao))

print("-=-"*20)
print(f"Lista de time dos Brasileirão: {times_brasileirao}")
print("-=-"*20)

print("-=-"*20)
print(f"Os 5 primeiros times são: {times_brasileirao[0:6]}")
print("-=-"*20)

print("-=-"*20)
print(f"Os 4 últimos times são: {times_brasileirao[16:]}")
print("-=-"*20)

print("-=-"*20)
print(f"A lista dos times do Brasileirão em Ordem Alfabética: {sorted(times_brasileirao)}")
print("-=-"*20)