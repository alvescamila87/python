# Entrada de dados
valor_hora = float(input("Informe o valor hora do colaborador: "))
qtd_horas = float(input("Informe a quantidade de horas trabalhadas do colaborador: "))

# Processamento de dados
salario = valor_hora * qtd_horas

# Saída de dados
print(f"Salário do mês: R${salario:.2f}, sendo: valor hora R$: {valor_hora:.2f} x {qtd_horas}hs trabalhadas no mês.")