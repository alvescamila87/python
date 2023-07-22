#estrutura de repetição: grupo da maioridade

from datetime import date

atual = date.today().year
total_maior = 0
total_menor = 0

for pessoa in range(1,8):
    ano_nascimento = int(input("Digite o ano que {}ª pessoa nasceu (AAAA): ".format(pessoa)))
    idade = atual - ano_nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1

print("Ao todo tivemos {} pessoas MAIORES de idade e {} MENORES e idade".format(total_maior, total_menor))