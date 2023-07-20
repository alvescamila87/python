#gerenciador de pagamentos

compras = float(input("Preço total das compras: R$"))

formas_pagamento = int(input('''
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão de crédito
[ 3 ] 2x no cartão de crédito                           
[ 4 ] 3x ou mais no cartão de crédito                             
Escolha uma das opções: '''))

if formas_pagamento == 1:
    print("Sua compra de R${:.2f} no pagamento à vista possui desconto e fica no valor de R${:.2f}.".format(compras, (compras - (compras * (10/100)))))
elif formas_pagamento == 2:
    print("Sua compra de R${:.2f} no pagamento à vista no cartão possui desconto e fica no valor de R${:.2f}.".format(compras, (compras - (compras * (5/100)))))
elif formas_pagamento == 3:
    print("Sua compra de R${:.2f} no pagamento em 2x no cartão de crédito terá duas parcelas de R${:.2f} mensais.".format(compras, (compras / 2)))
elif formas_pagamento == 4:
    parcelas = int(input("Quantas parcelas? "))
    if parcelas == 1:
        print("Sua compra de R${:.2f} no pagamento à vista no cartão possui desconto e fica no valor de R${:.2f}.".format(compras, (compras - (compras * (5/100)))))
    elif parcelas == 2:
        print("Sua compra de R${:.2f} no pagamento em 2x no cartão de crédito terá duas parcelas de R${:.2f} mensais.".format(compras, (compras / 2)))
    elif parcelas >= 3:
        print("Sua compra será parcelada em {}x de R${:.2f} com JUROS!".format(parcelas, ((compras + (compras * 20/100))) / parcelas ))
        print("Sua compra de R${:.2f} no pagamento em {}x no cartão de crédito terá {} parcelas de R${:.2f} mensais.".format(compras, parcelas, parcelas, ((compras + (compras * 20/100))) / parcelas ))
    else:
        total = 0
        print("Opção inválida de pagamento. Tente novamente!")
else:
    total = 0
    print("Opção inválida de pagamento. Tente novamente!")
        

#outra forma de resolver

print('{:=^40}'.format('LOJAS ALVES'))

preco = float(input("Preço total das compras: R$"))

print('''
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão de crédito
[ 3 ] 2x no cartão de crédito                           
[ 4 ] 3x ou mais no cartão de crédito                             
Escolha uma das opções: ''')

opcao = int(input("Escolha uma das opções: "))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f} SEM juros.".format(parcela))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_parcelas = int(input("Quantas parcelas? "))
    parcela = total / total_parcelas
    print("Sua compra será parcelada em {}x de R${:.2f} COM juros.".format(total_parcelas, parcela))
else:
    total = 0
    print("Opção inválida de pagamento. Tente novamente!")
print("Sua compra de R${:.2f} vai custar R${:2.f} no final.".format(preco, total))
