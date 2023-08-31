# Entrada de dados
num1 = int(input("Informe um número inteiro para N1: "))
num2 = int(input("Informe um número inteiro para N2: "))
num3 = float(input("Informe um número fracionado para N3: "))

# Processamento de dados
# a) o produto do dobro do primeiro com metade do segundo.
dobro_num1 = num1 * 2
metade_num2 = num2 / 2
produto_a = dobro_num1 + metade_num2



# b) a soma do triplo do primeiro com o terceiro.
triplo_num1 = num1 * 3
triplo_num3 = num3 * 3
produto_b = triplo_num1 + triplo_num3


# c) o terceiro elevado ao cubo.
cubo_num3 = num3**3

# Saída de dados
print(produto_a)
print(produto_b)
print(cubo_num3)


