num = int(input('Informe um número: '))
soma = 0

while num != 0:
    digito = num % 10 #encontrar último dígito
    num = (num - digito) // 10 #encontrar resto do número
    soma = soma + digito
print(soma)