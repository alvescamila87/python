# Entrada de dados

area = float(input("Informe o tamanho em metros quadrados da área a ser pintada: m² "))

# Latas 18lts

if area % 108 == 0:
    latas = area / 108
elif area % 108 != 0:
    latas = int(area / 108) + 1

valor_latas = latas * 80

# Galões 3.6tls
if area % 21 == 0:
    galoes = area / 21
elif area % 21 != 0:
    galoes = int(area / 21) + 1

valor_galoes = galoes * 25


print(f"Opção LATA: Comprar apenas latas de 18 litros: qtd latas {latas}, valor R${valor_latas}.")
print(f"Opção GALÃO: - Comprar apenas galões de 3,6 litros: qtd galões {galoes}, valor R${valor_galoes}.")

# Misturar latas 18lts e galões 3.6tls
import math

litros_lata = 18
litros_galao = 3.6
valor_lata = 80
valor_galao = 25

consumo_litros = area / 6 * 1.1

qtd_lata_misto = consumo_litros // litros_lata
qtd_galao_misto = math.ceil((consumo_litros - qtd_lata_misto * litros_lata) / litros_galao)
valor_lata_misto = qtd_lata_misto * valor_lata
valor_galao_misto = qtd_galao_misto * valor_galao
print("Opção MISTA 'LATAS E GALÕES:")
print(' - Para menor menor desperdício de tinta, relatório:')
print(f' - Quantidade latas: {qtd_lata_misto:.0f}')
print(f' - Quantidade galões: {qtd_galao_misto:.0f}')
print(f' - Quantidade total mistas: {qtd_lata_misto + qtd_galao_misto:.0f}')
print(f' - Valor total misto: R${valor_lata_misto + valor_galao_misto:.2f}.')
