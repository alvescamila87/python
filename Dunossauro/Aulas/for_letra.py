palavra = "Karoline"

for letra in palavra:
    if letra == "a":
        print("vogal")
    elif letra == "e":
        print("vogal")
    elif letra == "i":
        print("vogal")
    elif letra == "o":
        print("vogal")
    elif letra == "u":
        print("vogal")
    else:
        print(letra)

# Opção 2
vogais = "aeiou"

for letra in palavra:
    if letra in vogais:
        print("vogal")
    else:
        print(letra)