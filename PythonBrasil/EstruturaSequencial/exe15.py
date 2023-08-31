# Entrada de dados
valor_hora = float(input("Informe o valor hora: "))
qtd_horas = int(input("Infome a quantidade de horas trabalhadas: (somente horas inteiras) "))

# Processamento de dados
salario_bruto = valor_hora * qtd_horas

inss_salario = salario_bruto * (1.08 / 100)

sindicato_salario = salario_bruto * (1.05 / 100)

ir_salario = salario_bruto * (1.11 / 100)

salario_liquido = salario_bruto - (inss_salario + sindicato_salario + ir_salario)


# Saída  de dados
print(f" + Salário Bruto: R${salario_bruto:.2f}")
print(f" - IR (11%): R${ir_salario:.2f}")
print(f" - INSS (8%): R${inss_salario:.2f}")
print(f" - Sindicato (5%): R${sindicato_salario:.2f}")
print(f" = Salário líquido: R${salario_liquido:.2f}")
