number = int(input('Digite um número: '))

while number != 0:
    lastDigit = number % 10
    beforeLastDigit = (number % 100) // 10

    numberWithoutLastDigit = number // 10
    number = numberWithoutLastDigit

    if (lastDigit == beforeLastDigit):
        print('sim')
        break

if (number == 0):
    print('não')
