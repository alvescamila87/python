#estrutura de bifurcacao: else 

poupanca = 500
saque = 200

if saque <= poupanca:
    print("Você sacou R$%d. Saldo atualizado: R$%d" %(saque, poupanca-saque))
else:
    print("Você não possui saldo suficiente para sacar o valor de R$%d " %saque)