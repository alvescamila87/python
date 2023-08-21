
palavra = 'Camila Alves'

# Utilizando for:
for letra in palavra:
    print(letra)

# Utilizando a posição de cada elemento:
for pos, letra in enumerate(palavra):
    print(pos, letra)

# Imprimindo apenas as palavras:
frase = 'Camila foi à feira'.split()

for palavra in frase:
    print(palavra)