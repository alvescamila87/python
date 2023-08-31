# Entrada de dados
pessoa = input("Informe se a pessoa é Homem ou Mulher: [H/M] ")

# Processamento de dados
if pessoa == "H" or pessoa == "h":
    # Calcular peso ideal para homens:
    altura = float(input("Informe a altura do homem: "))
    peso_ideal_homem = (72.7 * altura) - 58
    # Saída de dados
    print(f"O peso ideal para uma homem de {altura:.2f}cm é de: {peso_ideal_homem:.2f}kg.")
elif pessoa == "M" or pessoa == "m":
    # Calcular peso ideal para mulheres:
    altura = float(input("Informe a altura da mulher: "))
    peso_ideal_mulher = (62.1 * altura) - 44.7
    # Saída de dados
    print(f"O peso ideal para uma mulher de {altura:.2f}cm é de: {peso_ideal_mulher:.2f}kg.")
else:
    # Saída de dados
    print("Opção inválida!. Só é possível informar H ou M.")

