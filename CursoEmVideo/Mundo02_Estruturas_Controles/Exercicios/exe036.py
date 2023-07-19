#empréstimo bancário

casa = float(input("Qual o valor da casa? "))

salario = float(input("Qual o seu salário? "))

tempo = int(input("Em até quantos anos você financiará o imóvel? "))

prestacao = casa / (tempo * 12)

minimo = salario * 30 / 100

print("Para financiar um imóvel de R${:.2f} em {} anos, o valor mensal da prestação será de R${:.2f}" .format(casa, tempo, prestacao))

if prestacao <= minimo:
    print("Empréstimo APROVADO! Prestação R${:.2f} Salário R${:.2f}".format(prestacao, salario))
else:
     print("Empréstimo NEGADO! A prestação mensal de R${:.2f} não pode exceder 30 por cento do seu salário mensal, que corresponde ao valor mínimo de R${:.2f}".format(prestacao, minimo))