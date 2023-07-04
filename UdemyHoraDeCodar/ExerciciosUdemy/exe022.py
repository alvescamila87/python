#numero maior

num1 = int(input('Informe um número: '))
num2 = int(input('Informe outro número: '))

if num2 > num1:
    print("O segundo número informado '%d' é maior que o primeiro '%d'" %(num2, num1))

if num1 > num2:
    print("O primeiro informado '%d' é maior que o segundo '%d'" %(num1, num2))

if num1 == num2:
    print("Os números informados são iguais!")