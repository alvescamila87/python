#estruturas compostas: número por extenso

numeros_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 
                 'cinco', 'seis', 'sete', 'oito', 'nove',
                 'dez', 'onze', 'doze', 'treze', 'catorze',
                 'quinze', 'dezesseis', 'dezessete', 'dezoite',
                 'dezenove', 'vinte')

print(numeros_extensos)

while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num >= 0 or num <= 20:
        print(f"Você informou o número {num} e por extenso fica: '{numeros_extensos[num]}'.")
    else:
        print("Número inválido. Tente novamente. ", end="")
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input("Quer continuar: [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print("Até logo!")



