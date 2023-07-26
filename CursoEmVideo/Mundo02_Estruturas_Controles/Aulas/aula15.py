#Estruturas de repetição:
#for, while and repeat (do while). Mas python só tem for e while

# while Verdadeiro:
#     caminha até a maça
# pega maça

# while True:
#     if possui terra:
#         caminha em frente
#     elif possui espaço vazio:
#         pula
#     elif possui moeda:
#         pega moeda
#     elif possui trofeu:
#         pega
#         break
# pega
# print('pegou trofeu')

#opção 1

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n

# print("A soma dos números informados vale {}.".format(s))
print(f"A soma dos números informados vale {s}.") #f-string

#f-strings
nome = "Camila"
idade = 35
salario = 987.35
print(f"A {nome} tem {idade} anos e ganha R${salario:.2f}") #python 3.6+
print("A {} tem {} anos.".format(nome, idade)) #python 3+
print("A %s tem %d anos." %(nome, idade)) #python 2+
