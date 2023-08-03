#estrutura de repetição: número primo

num = int(input("Digite um número: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0: #numero divisível 2 vezes (por 1 e por ele mesmo)
        print('\033[33m', end="")
        total += 1
    else:
        print('\033[31m', end="")
    print("{} ".format(c), end="")
print("\n\033[mO número {} foi divisível {} vezes.".format(num, total))

if total == 2: #numero divisível 2 vezes (por 1 e por ele mesmo)
    print("E por isso ele é PRIMO!")
else:
    print("E por isso ele NÃO é primo.") #1 não é número primo