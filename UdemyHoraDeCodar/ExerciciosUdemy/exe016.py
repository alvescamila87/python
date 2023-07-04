#float

salario = float(input("Informe o salário: "))
aumento = float(input("Informe o percentual de aumento: "))
novo_salario = salario + (salario * (aumento / 100))
print("Você recebeu aumento de %.2f por cento e seu novo salário é de R$%.2f." %(aumento, novo_salario))