#elif

nome = input("Digite seu nome: ")

if nome == "Camila":
    print("Você é um admin")

elif nome == "Maria":
    print("Você é um manager")

else:
    print("Você é um usuário comum!")

numero = int(input("Informe um número: "))

if numero > 0 and numero < 5:
    print("Maior que 0")
elif numero > 5 and numero < 10:
    print("Maior que 5")
elif numero > 10:
    print("Maior que 10")
else:
    print("Número negativo")