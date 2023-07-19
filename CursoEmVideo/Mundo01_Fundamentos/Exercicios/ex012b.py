produto=float(input('informe o preço do produto R$:'))
oferta=produto - (produto*5/100)
print('O produto de R${:.2f} possui 5% desconto, saindo a R${:.2f}'.format(produto, oferta))
