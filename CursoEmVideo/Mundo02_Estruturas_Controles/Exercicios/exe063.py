#estrutura de repetição: sequência de fibonacci v1

print("-"*30)    
print("Sequência de Fibonacci")
print("-"*30)    

termos = int(input("Quantos termos você que seja exibido? "))
termo1 = 0
termo2 = 1
print('~'*30)
print('{} -> {}'.format(termo1, termo2), end="")
contador = 3

while contador <= termos:
    termo3 = termo1 + termo2
    print(" -> {}".format(termo3), end="")
    termo1 = termo2
    termo2 = termo3
    contador += 1
print("-> FIM")

