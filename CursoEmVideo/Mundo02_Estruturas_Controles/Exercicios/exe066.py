#estrutura de repetição: vários números com flag

# num = 0
soma = 0
contador = 0

while True:
    num = int(input("Digite um valor (999 para parar): "))
    if num == 999:
        break
    contador += 1    
    soma += num

print(f"A soma dos {contador} números foi de {soma}.")

