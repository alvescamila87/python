
frase = str(input("Digite uma frase: ")).strip().upper()
print(frase)

palavras = frase.split()
print(palavras)

junto = "".join(palavras)
print(junto)

# for letra in range(len(junto) -1, -1, -1):
#      print(junto[letra])