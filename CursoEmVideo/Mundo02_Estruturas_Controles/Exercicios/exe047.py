#estrutura de repetição: exercício contagem de pares

for par in range(2,51,2):
    print(par, end=' ')
print("Acabou!") 

#outra forma de resolver
for n in range(1,51):
    if n % 2 == 0:
        print(n, end=' ') 
print("Acabou!") 