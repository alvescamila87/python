# Entrada de dados
temperatura_f = float(input("Informe  a temperatura em graus Fahrenheit (Fº): "))

# Processamento de dados
celsius = 5 * ((temperatura_f - 32) / 9)

# Saída de dados
print(f"A temperatura de {temperatura_f:.2f} (Fº) Fahrenheit corresponde à {celsius:.2f} (Cº) em graus Celsius.")