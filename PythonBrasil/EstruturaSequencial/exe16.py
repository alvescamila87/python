# Entrada de dados
area = float(input("Informe o tamanho em metros quadrados da área a ser pintada: m² "))

# Processamento de dados:
if area % 54 == 0:
    latas = area / 54
else:
    latas = int(area / 54) + 1

valor = latas * 80

# Saída de dados
print(f"Área: {area:.2f}m²")
print(f"Quantidades de latas de tinta a serem compradas: {latas:.2f}, preço total R${valor:.2f}.")