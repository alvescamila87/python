#Estruturas compostas: Dicionários {} - EXERCÍCIO: Cadastro de trabalhador python

from datetime import date, datetime

# Opção Camila

trabalhador = dict()

trabalhador["nome"] = str(input("Nome: "))
trabalhador["ano de nascimento"] = int(input("Ano de nascimento: "))
ano_atual = date.today().year
trabalhador["idade"] = (ano_atual - trabalhador["ano de nascimento"])
trabalhador["ctps"] = int(input("Informe o nº da Carteira de Trabalho (CTPS). [Informe '0' caso não tenha]: "))
if trabalhador["ctps"] != 0:
    trabalhador["ano de contratacao"] = int(input("Ano de contratação: "))
    trabalhador["salario"] = float(input("Salário: R$"))
    trabalhador["aposentadoria"] = trabalhador["idade"] + ((trabalhador["ano de contratacao"] + 35) - ano_atual)
print("-="*30)
for k, v in trabalhador.items():
    print(f" - {k} tem valor {v}.")


# Opção Guanabara:

dados = dict()

dados["nome"] = str(input("Nome: "))
nasc = int(input("Ano de nascimento: "))
dados["idade"] = (datetime.now().year - nasc)
dados["ctps"] = int(input("Informe o nº da Carteira de Trabalho (CTPS). [Informe '0' caso não tenha]: "))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input("Ano de contratação: "))
    dados["salario"] = float(input("Salário: R$"))
    dados["aposentadoria"] = dados["idade"] + ((dados["contratacao"] + 35) - datetime.now().year)
print("-="*30)
for k, v in dados.items():
    print(f" - {k} tem valor {v}.")