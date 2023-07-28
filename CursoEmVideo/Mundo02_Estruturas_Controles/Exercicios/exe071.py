#estrutura de repetição: simulador de caixa eletrônico

# Opção 1 de resolução
# print('='*40)
# print('{:^40}'.format(' BANCO CEV '))
# print('='*40)


# saque = int(input("Informe a quantia a sacar: R$"))

# valor_saque = saque
# nota_50 = 0
# nota_20 = 0
# nota_10 = 0
# nota_1 = 0


# while True:
#     while saque >= 50:
#         nota_50 = nota_50 + 1
#         saque = saque - 50
#     while saque >= 20:
#         nota_20 = nota_20 + 1
#         saque = saque - 20
#     while saque >= 10:
#         nota_10 = nota_10 + 1
#         saque = saque - 10
#     while saque >= 1:
#         nota_1 = nota_1 + 1
#         saque = saque - 1
#     if valor_saque == 0:
#         break

# print(f'''Saque solicitado: R${valor_saque:.2f}. 
#       Você receberá:
#       {nota_50} notas de R$ 50,00;
#       {nota_20} notas de R$ 20,00;
#       {nota_10} notas de R$ 10,00;
#       {nota_1} notas de R$  1,00;
#       ''')

# Opção 2 de resolução
print('='*40)
print('{:^40}'.format(' BANCO CEV '))
print('='*40)

valor_saque = int(input("Que valor você quer sacar? R$"))
total_saque = valor_saque
cedula = 50
total_celulas = 0

while True:
    if total_saque >= cedula:
        total_saque -= cedula
        total_celulas += 1
    else:
        if total_celulas > 0:
            print(f"Total de {total_celulas} cédulas de R${cedula}")
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_celulas = 0
        if total_saque == 0:
            break
print('='*40)
print("Volte sempre ao BANCO CEV!")



