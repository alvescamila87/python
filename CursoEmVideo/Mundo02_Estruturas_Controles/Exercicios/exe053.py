#estrutura de repetição: detector de palídromo

frase = str(input("Digite uma frase: ")).strip().upper() #tirar espaços e jogar para maiúscula

#dividir a frase em palavras para gerar lista
palavras = frase.split()
print("Você digitou: {}".format(palavras))

#juntar as palavras SEM espaços internos
junto = ''.join(palavras)
print("Você digitou: {}".format(junto))

#inverso
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada NÃO é um palíndromo.")


#outra forma de fazer:
inverso = junto[::-1]
print(junto, inverso)
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada NÃO é um palíndromo.")



#codewar
for letra in range(len(junto) -1, -1, -1):
    print(junto[letra])