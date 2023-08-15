# Exception: EXERCÍCIO Funções aprofundadas em Python

def valida_numero_inteiro(msg):
    while True:
        try:
            entrada_inteiro = int(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Favor digitar um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[31mERRO: Entrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return entrada_inteiro

def valida_numero_real(msg):
    while True:
        try:
            entrada_real = float(input(msg))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Favor digitar um número real válido.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[31mERRO: Entrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return entrada_real

m = valida_numero_inteiro("Digite um número inteiro: ")
n = valida_numero_real("Digite um número real:")
print(f"Você digitou o valor inteiro: {m}.")
print(f"Você digitou o valor real: {n}.")









