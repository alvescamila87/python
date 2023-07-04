#produtos

categoria_produto = int(input("Informe o número do produto: "))

if categoria_produto == 1:
    print("A categoria de produto %d é BOLSA" %categoria_produto)
elif categoria_produto == 2:
    print("A categoria de produto %d é TÊNIS" %categoria_produto)
elif categoria_produto == 3:
    print("A categoria de produto %d é MOCHILA" %categoria_produto)
else:
    print("A categoria informada NÃO foi encontrada.")