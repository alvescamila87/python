#lista média das notas

notas = [8.5, 9, 10, 7, 5.5]

i = 0
soma_notas = 0

while i < 5:
    soma_notas = soma_notas + notas[i] #soma as notas na variável
    i = i + 1

media = soma_notas / 5 #com a soma, calcula a média

print("O aluno obteve a média %.2f" %media)
    