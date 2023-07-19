#classificação de atletas

from datetime import date
atual = date.today().year

ano_nascimento = int(input("Ano nascimento do atleta: "))

idade = atual - ano_nascimento

# if idade > 25:
#     print("Classificação do atleta: MASTER")
# elif idade <= 25 and idade > 19: 
#     print("Classificação do atleta: SÊNIOR")
# elif idade <= 19 and idade > 14: 
#     print("Classificação do atleta: JUNIOR")
# elif idade <= 14 and idade > 9: 
#     print("Classificação do atleta: INFANTIL")
# elif idade <= 9:
#     print("Classificação do atleta: MIRIM")

#OUTRA FORMA DE RESOLVER

if idade <= 9:
    print("Classificação do atleta: MIRIM")
elif idade <= 14: 
    print("Classificação do atleta: INFANTIL")
elif idade <= 19: 
    print("Classificação do atleta: JUNIOR")
elif idade <= 25: 
    print("Classificação do atleta: SÊNIOR")
else:
    print("Classificação do atleta: MASTER")
