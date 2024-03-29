# Funções PARTE 2 - Exercício: Função para Fatorial

def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Exibe ou não a fórmula do Fatorial! do número.
    :return: O valor do Fatorial de um número 'num'.
    Função criada no CursoEmVídeo (Guanabara)
    """
    print('-'*20)
    f = 1
    for c in range(num, 0, -1):
       if show:
            print(c, end="")
            if c > 1:
                print(" x ", end="")
            else:
                print(" = ", end="")
       f *= c
    return f


# Programa principal
n = int(input("Informe um número que você deseja o fatorial: "))
print(fatorial(n, True))
help(fatorial)

# Opção 2 (Criar fatorial)

def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")