#imc - índice de massa corpórea

peso = float(input("Qual seu peso? (Kg) "))

altura = float(input("Qual sua altura? (m) "))

imc = peso / (altura ** 2)

if imc <= 18.5:
    print("Seu IMC: {:.2f}kg/m² - Classificação: Abaixo do peso.". format(imc))
elif imc <= 25:
    print("Seu IMC: {:.2f}kg/m² - Classificação: Peso ideal.". format(imc))
elif imc <= 30:
    print("Seu IMC: {:.2f}kg/m² - Classificação: Sobrepeso.". format(imc))
elif imc <= 40:
    print("Seu IMC: {:.2f}kg/m² - Classificação: Obesidade.". format(imc))
else:
    print("Seu IMC: {:.2f}kg/m² - Classificação: Obesidade mórbida.". format(imc))