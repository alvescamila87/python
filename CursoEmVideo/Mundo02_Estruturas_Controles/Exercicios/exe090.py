#Estruturas compostas: Dicionários {} - EXERCÍCIO: Dicionário Python

aluno = dict()

aluno["nome"] = str(input("Nome: "))
aluno["media"] = float(input(f"Média de {aluno['nome']}:  "))

print("-="*30)
print(f" - nome é igual a {aluno['nome']}")
print(f" - média é igual a {aluno['media']}")
if aluno["media"] >= 7:
    aluno["situação"] = "Aprovado"
elif aluno["media"] <= 5 or aluno["media"] < 7:
    aluno["situação"] = "Recuperação"
else:
    aluno["situação"] = "Reprovado"

print(f" - situação é igual a {aluno['situação']}")