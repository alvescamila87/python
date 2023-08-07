#Estruturas compostas: Dicionários {} - EXERCÍCIO: Cadastro de trabalhador python

from datetime import date

trabalhador = dict()

trabalhador["nome"] = str(input("Nome: "))
trabalhador["ano de nascimento"] = int(input("Ano de nascimento: "))
ano_atual = date.today().year
trabalhador["idade"] = (ano_atual - trabalhador["ano de nascimento"])
trabalhador["ctps"] = int(input("Informe o nº da Carteira de Trabalho (CTPS). [Informe '0' caso não tenha]: "))
trabalhador["ano de contratacao"] = int(input("Ano de contratação: "))
trabalhador["aposentadoria"] = 2043
trabalhador["salario"] = float(input("Salário: R$"))

print(trabalhador)

print(f'- nome tem o valor {trabalhador["nome"]}')
print(f'- idade tem o valor {trabalhador["idade"]}')
print(f'- ctps tem o valor de {trabalhador["ctps"]}')
if trabalhador["ctps"] != 0:
    print(f'- contratação tem o valor de {trabalhador["ano de contratacao"]}')
    print(f'- salario tem o valor de R${trabalhador["salario"]}')
    print(f'- aposentadoria tem o valor de {trabalhador["aposentadoria"]}')

