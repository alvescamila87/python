#lista de itens

lista = ["Fusca", "Gol", "Audi", "Jetta", "Polo", "T-Cross", "Nivus", "Land Rover"]

x = 0

item_procurado_1 = str(input("Informe um veículo: "))
item_procurado_2 = str(input("Informe outro veículo: "))

while x < len(lista):
    if lista[x] == item_procurado_1:
        print("O veículo %s foi encontrado antes" %item_procurado_1)
        break
    elif lista[x] == item_procurado_2:
        print("O veículo %s foi encontrado antes." %item_procurado_2)
        break
    
    x = x + 1
