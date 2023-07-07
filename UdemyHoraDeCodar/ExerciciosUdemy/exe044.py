#lista com for

lista = ["Camiseta", "Calça", "Meia", "Casaco", "Jeans", "Cinto", "Tênis"]

item_procurado = str(input("Informa um item de vestuário: "))

for item in lista:
    if item == item_procurado:
        print("O item %s foi encontrado!" %item_procurado)
    else:
        print("O item %s não foi encontrado na lista" %item_procurado)
        break
    
