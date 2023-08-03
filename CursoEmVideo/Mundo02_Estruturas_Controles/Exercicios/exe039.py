#alistamento militar

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input("Ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade > 18: 
    print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, ano_atual))
    print("Você já deveria ter se alistado ao serviço militar há {} anos.".format(idade - 18))
    print("Seu alistamento foi em {}.".format(ano_nascimento + 18))
elif idade == 18:
    print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, ano_atual))
    print("Você tem que se alistar imediatamente!!!")
elif idade < 18:
    print("Quem nasceu em {} tem {} anos em {}".format(ano_nascimento, idade, ano_atual))
    print("Ainda falta {} anos para o alistamento ao serviço militar." .format((18 - idade)))
    print("Seu alistamento será em {}.".format(ano_nascimento + 18))


