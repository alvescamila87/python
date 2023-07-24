
frase = str(input("Digite uma frase: ")).strip().upper()
print(frase)

palavras = frase.split()
print(palavras)

# junto = "".join(palavras)
# print(junto)

for letra in range(len(palavras) -1, -1, -1):
     print(palavras[letra])