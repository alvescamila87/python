#estrutura de repetição: progressão aritmética v3

primeiro_termo = int(input("Primeiro termo da PA: "))
razao = int(input("Razão da PA: "))
termo = primeiro_termo
contador = 1
total_termos = 0
novo_termo = 10

while novo_termo != 0: 
    total_termos += novo_termo
    while contador <= total_termos:
        print("{} -> ".format(termo), end="")
        termo += razao
        contador += 1
    print("PAUSA")
    
    novo_termo = int(input("Quantos termos você quer mostrar a mais? "))


print("FIM da PA com {} termos exbidos.".format(total_termos))


    