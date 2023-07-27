#estrutura de repetição: estatística em produtos

print("-"*30)
print("LOJA SUPER BARATÃO")    
print("-"*30)

soma = 0
contador = 0
maior_valor = 0
menor_valor = 0
nome_produto_barato = ''


while True:
    produto = str(input("Nome do produto: ")).strip()
    valor = float(input("Preço: R$"))
    soma += valor
    if contador == 1 or valor < menor_valor:
        menor_valor = valor
        nome_produto_barato = produto
    if valor >= 1000:
        contador += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if continuar == "N":
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f"O total da compra foi de R${soma:.2f}.")
print(f"Temos {contador} produtos custando mais de R$1.000,00.'")
print(f"O produto mais barato foi '{nome_produto_barato}' que custa R${menor_valor}.")