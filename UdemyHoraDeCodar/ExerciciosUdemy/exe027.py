#renda de usuário

renda_usuario = float(input("Informa o valor da sua renda R$: "))

if renda_usuario < 2000:
    print("Para a renda de R$%.2f, o limite de cartão de crédito é de 'R$ 1.000,00'." %renda_usuario)

elif renda_usuario >= 2000 and renda_usuario < 4000:
    print("Para a renda de R$%.2f, o limite do cartão de crédito é de 'R$2.000,00'." %renda_usuario)

elif renda_usuario >= 4000 and renda_usuario < 10000:
    print("Para a renda de R$%.2f, o limite do cartão de crédito é de 'R$3.000,00'." %renda_usuario)
    
else:
    print("Para a renda de R$%.2f, entrar em contato com o gerente da sua conta bancária." %renda_usuario)

#ou pode ser feito:

renda = float(input("Informa o valor da sua renda R$: "))
limite = 0

if renda < 2000:
    limite = 1000
elif renda < 4000:
    limite = 2000
elif renda < 10000:
    limite = 3000
elif renda > 10000:
    limite = 3000
    print("Você precisa falar com  nosso gerente")

print("O seu cartão foi aprovado e o limite é de R$%d" %limite)