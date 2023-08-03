#Estruturas de repetição while:
#Laço de repetição com teste lógico
#"while não"(enquanto não é utilizado quando não se sabe o limite/intervalo)



# while not maça:
#     caminha até a maça
# pega maça

# while not maça:
#     if possui terra:
#         caminha em frente
#     elif possui espaço vazio:
#         pula
#     elif possui moeda:
#         pega moeda
# pega maça
# print('pegou a maça')

#exemplo 1 - for
for c in range (1,10):
    print(c)
print("Fim")

#exemplo 2 - while
c = 1
while c < 10:
    print(c)
    c += 1
print("Fim")

#ponto de parada/limite/flag
n = 1
while n != 0:
    n = int(input("Digite um valor: "))
print("Fim")

#exemplo 3
resposta = "S"
while resposta == "S":
    n = int(input("Digite um valor: "))
    resposta = str(input("Quer continuar? [S/N]")).strip().upper()[0]
print("Fim")

#exemplo 4
n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0: 
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} impares.".format(par, impar))