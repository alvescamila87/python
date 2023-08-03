#estrutura de repetição: progressão aritmética v2

primeiro_termo = int(input("Informe o PRIMEIRO TERMO da PA(Progressão Aritmética): "))
razao = int(input("Informe a RAZÃO da PA(Progressão Aritmética): "))
termo = primeiro_termo
contador = 1

while contador <= 10:
    print("{} -> " .format(termo), end="")
    termo += razao
    contador += 1

print("FIM")


    