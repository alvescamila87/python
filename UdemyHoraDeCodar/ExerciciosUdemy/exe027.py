#renda de usuário

renda_usuario = float(input("Informa o valor da sua renda R$: "))

if renda_usuario < 2000:
    print("Para a renda de R$%.2f, o limite de cartão de crédito é de 'R$ 1.000,00'." %renda_usuario)

elif renda_usuario >= 2000 and renda_usuario < 4000:
    print("Para a renda de R$%.2f, o limite do cartão de crédito é de 'R$2.000,00'." %renda_usuario)

elif renda_usuario >= 4000 and renda_usuario < 6000:
    print("Para a renda de R$%.2f, o limite do cartão de crédito é de 'R$3.000,00'." %renda_usuario)
    
else:
    print("Para a renda de R$%.2f, entrar em contato com o gerente da sua conta bancária." %renda_usuario)