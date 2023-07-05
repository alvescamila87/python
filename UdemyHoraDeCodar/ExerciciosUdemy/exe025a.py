#if aninhado número maior que 10

num = int(input("Informe um número: "))

if num > 10:
    if num < 20:
        print("Multiplicação do seu número %d por 2 é %d" %(num, num * 2))
    else:
        print("Multiplicação do seu número %d por 5 é %d" %(num, num * 5))
else:
    print("Para prosseguir, o número precisa ser maior que '10'.")