#comparar números

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

if num1 > num2:
    print("O primeiro número '{}' é MAIOR que o segundo '{}'.".format(num1, num2))
elif num2 > num1:
    print("O segundo número '{}' é MAIOR que o primeiro '{}'.".format(num2, num1))
elif num1 == num2:
    print("Os números informados '{}' e '{}' são IGUAIS.". format(num1, num2)) 