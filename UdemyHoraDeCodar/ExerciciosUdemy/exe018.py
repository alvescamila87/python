#deposito bancário

saldo = float(359.56)
novo_valor = float(input("Informe o valor do depósito: "))
cartao_credito = float(125.98)

novo_saldo = print("Saldo anterior R$%.2f. Cartão de crédito R$%.2f. Com o depósito de R$%.2f novo saldo da sua conta bancária é de R$%.2f." %(saldo, cartao_credito, novo_valor, saldo + novo_valor - cartao_credito))


