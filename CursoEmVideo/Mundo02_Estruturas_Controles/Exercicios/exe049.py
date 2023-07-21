#estrutura de repetição: exercício tabuada v2
tabuada = int(input("Digite um número para ver a tabuada: "))

for num in range(1,11):
    print("{} X {:2} = {}".format(tabuada, num, num*tabuada))
