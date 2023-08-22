#tupla

#desempacotar tupla:
minha_tupla = ('Camila', 35)

nome, idade = minha_tupla

print(nome)
print(idade)

#desempacotar tupla modo 2:
minha_tupla_2 = ('Camila', 35, "Endereço", 262)

nome2, idade2, *empacotar_dados = minha_tupla_2

print(nome2)
print(idade2)
print(empacotar_dados)

# desempacotar triangulando:
minha_tupla_3 = ('Karoline', 36)

nome3, idade3 = minha_tupla_3

print(nome3, idade3)

nome3, idade3 = idade3, nome3
print(nome3) #triangulou
print(idade3) #triangulou

# ter mais de um retorno em tupla

def minha_func():
    return 1, 2, 3

print(minha_func())