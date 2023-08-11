# Função: EXERCÍCIO: Função que descobre o maior

from time import sleep


def maiorValor(* numeros):
    maior_numero = 0
    print("-=" * 30)
    print("Analisando os valores passados...")
    sleep(1)
    for num in numeros:
        print(f"{num} ", end="", flush=True)
        sleep(0.3)
    print(f"Foram informados {len(numeros)} números ao todo.")
    # if len(numeros) == 0:
    #     maior_numero = num
    # else:
    #     if num > maior_numero:
    #         maior_numero = num
    if len(numeros) > 0:
        print(f'{max(numeros)}')
    else:
        print("Não foi passado valor")
    print(f"O maior valor informado foi '{maior_numero}'.")
    sleep(0.5)


# Programa principal
maiorValor(2,3,5,6)
maiorValor(50,2,6,8,105,5555)
maiorValor(0)
maiorValor()