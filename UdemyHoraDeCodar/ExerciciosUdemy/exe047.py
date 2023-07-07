#lista dentro de lista

produto_vestuario = ["Camiseta", "Azul", 30]

produto_calcado = ["Tênis", "Branco", 150] 

produto_acessorio = ["Cinto", "Preto", 20]

lista_produtos = [produto_calcado, produto_acessorio, produto_vestuario]

for produto in lista_produtos:
    print("O produto é %s e tem a cor %s o seu preço é R$%.2f." % (produto[0], produto[1], produto[2]))