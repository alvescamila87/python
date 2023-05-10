#Numeros Adjacentes iguais

number = int(input('Digite um número'))

while number != 0:
    lastDigit = number % 10
    beforeLastDigit = (number % 100) // 10

    numberWithoutLastDigit = number // 10
    number = numberWithoutLastDigit

    if (lastDigit == beforeLastDigit):
        print('Esse número digitado possui dígitos adjacentes iguais!')
        break

if (number == 0):
    print('Esse número digitado NÃO possui dígitos adjacentes iguais...')



