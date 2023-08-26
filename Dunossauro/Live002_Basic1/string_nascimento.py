
data = str(input("Informe a data de nascimento: [dd/mm/aaaa] "))

dia, mes, ano = data.split("/")

print(f"Nasceu em {dia} de {mes} de{ano}.")
