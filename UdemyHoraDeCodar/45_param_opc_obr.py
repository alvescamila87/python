#parametro obrigatório e opcional

def soma_numeros(a, b, c = 10):
    print(a + b + c)

#ignora o 'c opcional' e utiliza o 'c = 3' dessa chamada da função
soma_numeros(1, 2, 3)

#utiliza o 'c opcional' pois na chamada da função não foi incomado o c
soma_numeros(10, 20)

#apresenta erro, pois o 'b' é um parametro obrigatório e não foi incomado, enquanto o 'c' é opcional
soma_numeros(10)