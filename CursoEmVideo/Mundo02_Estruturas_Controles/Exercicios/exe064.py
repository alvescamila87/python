#estrutura de repetição: tratando vários valores v1

num = contador = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    contador += 1
    soma += num
    num = int(input("Digite um número [999 para parar]: "))
    
print("Você digitou {} números e a soma entre eles foi de {}.".format(contador, soma))


