#numero maior que 10

num = int(input("Informe um número: "))

if num > 10:
    if num < 20:
        print("Menor que 20")
        print("%d" %(num * 2))
    else:
        print("Maior que 20")
        print("%d" %(num * 5))
else:
    print("Para prosseguir, o número precisa ser maior que 10!")