
data = str(input("Informe a data de nascimento: [dd/mm/aaaa] "))

dia, mes, ano = data.replace("/", " ")

print(dia, mes, ano)