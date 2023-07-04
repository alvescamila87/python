#salario

salario = float(input("Informa o valor do salário R$: "))

if salario > 1800:
    print("Você precisa pagar imposto de renda sobre o salário de R$%.2F" %salario)
else:
    print("Seu salário está isento de IR!")