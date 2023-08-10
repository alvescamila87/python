# Função: EXERCÍCIO: Função contador

from time import sleep

def contador(i, f, p):
    print("-="*20)
    print(f"Contagem de {i} até {f} de {p} em {p}:")
    #sleep(2.5)
    if i < f:
        contador = i
        while contador <= f:
            print(f"{contador} ", end="", flush=True) #Para não ligar buffer de tela (ficar esperando a contagem)
            sleep(0.5)
            contador += p
        print("FIM!")
    else:
        contador = i
        while contador >= f:
            print(f'{contador} ', end="", flush=True) #Para não ligar buffer de tela (ficar esperando a contagem)
            sleep(0.5)
            contador -= p
        print("FIM!")


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print("Agora é a sua vez de personalizar a contagem!")
inicio = int(input("Início: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
contador(i = inicio, f = fim, p = passo)