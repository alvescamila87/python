#estrutura de repetição: jogo do par ou ímpar

from random import randint

print("-="*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("-="*20)

soma = 0
contador = 0

while True:
    jogador = int(input("Diga um valor: "))
    computador = randint(0,10)
    soma = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? P/I ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}. Total de {soma} ", end='')
    print("DEU PAR" if soma % 2 == 0 else "DEU ÍMPAR")
    if tipo == "P":
        if soma % 2 == 0:
            print("Você venceu!")
            contador += 1
        else:
            print("Você perdeu!")
            break
    elif tipo == "I":
        if soma % 2 == 1:
            print("Você venceu!")
            contador += 1
        else:
            print("Você perdeu!")
            break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {contador} vezes.")

    