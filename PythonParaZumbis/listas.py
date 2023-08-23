notas = []
k = 0
soma = 0

while k <= 3:
    notas.append(float(input(f"Informe a nota da prova {k+1}: ")))
    soma = soma + notas[k]
    k = k + 1

print(f"Soma de notas: {soma} e média de notas: {soma/len(notas)}.")