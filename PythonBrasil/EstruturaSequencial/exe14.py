# Entrada de dados
peso_peixe = float(input("Informe o peso de peixes: (kg) "))

# Processamento de dados
if peso_peixe > 50:
    peso_excedente = peso_peixe - 50
    multa = peso_excedente * 4.00
    # Saída de dados
    print(f"A pesca rendeu: {peso_peixe:.2f} kg de peixe.")
    print("Esse peso está ACIMA do regulamento do estado de SP que são 50kg.")
    print(f"Peso excedente de peixe: {peso_excedente:.2f} kg. Multa a pagar R${multa:.2f} sobre o peso excedente.")
else:
    # Saída de dados
    print(f"{peso_peixe:.2f} kg de peixe. Obrigada!")