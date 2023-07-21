#estrutura de repetição: progressão aritmética

termo = int(input("Informe o PRIMEIRO TERMO da PA(Progressão Aritmética): "))
razao = int(input("Informe a RAZÃO da PA(Progressão Aritmética): "))
decimo = termo + (10 - 1) * razao #cálculo do 10º termo de uma PA


for num in range(termo,decimo + razao,razao):
    print("{} ".format(num), end="-> ")

print("ACABOU")