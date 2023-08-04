#Parte 2: Estruturas compostas -> Boletim com listas compostas

alunos = list()

while True:
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break

print("-="*30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print("-="*30)
for indice, a in enumerate(alunos):
    print(f"{indice:<4}{a[0]:<10}{a[2]:>8.1f}")

# Mostrar notas individualmente
while True:
    print("-"*35)
    opcao = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if opcao == 999:
        print("FINALIZANDO...")
        break
    if opcao <= len(alunos) - 1:
        print(f"Notas de {alunos[opcao][0]} são {alunos[opcao][1]}")
print("<<< VOLTE SEMPRE >>>")
