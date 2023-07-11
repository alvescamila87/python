#manipulação de strings: checando inicio da string: startswith e endswith

frase = "Testamos o começo da string"

#checa a primeira palavra da string frase
print(frase.startswith("Testamos"))

print(frase.startswith("string"))

#é possível criar condicionais:
if(frase.startswith("Testamos") == True):
    print("Encontramos a primeira palavra!")
else:
    print("Tente outra palavra da frase...")

#checa a última palavra da string frase
print(frase.endswith("string"))

print(frase.endswith("Testamos"))



