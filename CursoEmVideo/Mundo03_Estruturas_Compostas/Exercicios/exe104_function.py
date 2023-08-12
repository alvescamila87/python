# Funções PARTE 2 - Exercício: Validando entrada de dados Python

def leiaInt(msg):
    """
    Lê se a informação recebida é um valor inteiro váldo.
    :param msg: recebe informação de 'n'.
    :return: retorna o valor de n caso esse for um número inteiro válido
    Função criada no CursoEmVídeo
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[m")
        if ok:
            break
    return valor

# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
