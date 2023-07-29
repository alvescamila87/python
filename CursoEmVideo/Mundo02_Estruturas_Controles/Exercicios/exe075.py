#estruturas compostas: Análise de dados em uma Tupla

num1 = int(input("Digite o 1º número: "))
num2 = int(input("Digite o 2º número: "))
num3 = int(input("Digite o 3º número: "))
num4 = int(input("Digite o 4º número: "))

numeros = (num1, num2, num3, num4)
print(f"Você digitou os valores: {numeros}")

print(f"O valor '9' apareceu {numeros.count(9)} vezes.")
if 3 in numeros:
    print(f"O valor '3' apareceu na {numeros.index(3)+1}ª posição.")
else:
    print("O valor '3' não foi digitado em nenhuma posição.")

print(f"Os valores pares digitados foram: ", end="")
for n in numeros:
    if n % 2 == 0:
        print(n, end=" ")


# opção 2 de resolução:

# tupla
# num = (int(input("Digite o um número: ")), 
#        int(input("Digite o outro número: ")), 
#        int(input("Digite o mais um número: ")), 
#        int(input("Digite o último número: ")), )