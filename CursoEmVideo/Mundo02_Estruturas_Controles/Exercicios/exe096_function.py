# Função: EXERCÍCIO: Função que calcula área



def area(larg, comp):
    a = larg * comp
    print(f"A área de um terreno {l}x{c} é de {a:.2f}m².")


# Programa principal
print(" Controle de Terrenos")
print("-" * 20)
l = float(input("LARGURA (m): "))
c = float(input("COMPRIMENTO (m): "))
area(l, c)
