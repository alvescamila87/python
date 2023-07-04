#if aninhado

idade = int(input("Qual é a sua idade? "))

if idade >= 18:
    print("Pode entrar na balada")

    #condição de IF aninhado
    metodo_pagamento = input("Você vai pagar com Dinheiro ou Cartão de Crédito? ")

    if metodo_pagamento == "dinheiro" or metodo_pagamento == "Dinheiro":
        print("Ir para fila nº 1")
    else:
        print("A fila de cartão é nº 2")

else:
    print("Você NÃO pode entrar na balada")