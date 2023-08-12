# Módulos e Pacotes:
# Modularização para aumentar a legibilidade e facilitar a manutenção


# 1) Modulos ('uteis.py')
def fatorial(n):
    f = 1
    for c in range(1,n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


# Programa principal
num = int(input("Digite um valor: "))
fat = fatorial(num)
print(f"O fatorial de {num} é {fat}.")



# 2) Formas de utilização dos módulos:

# Exemplo 1:
# 1.1 Criar dois arquivos em um diretório: sendo um para as funções e outro para a execução do programa
# 1.2 No arquivo de execução do programa, no cabeçalho escreva:
# import uteis
# 1.3 Na execução do 'programa principal', identifique os comandos/módulos.
# uteis.fatorial(num)
# uteis.dobro(num)
# uteis.triplo(num)

# Exemplo 2:
# 1.1 Criar dois arquivos em um diretório: sendo um para as funções e outro para a execução do programa
# 1.2 No arquivo de execução do programa, no cabeçalho escreva:
# from uteis uteis fatorial, dobro, triplo
# 1.3 Na execução do 'programa principal', apenas descreva as funções do módulo:
# fatorial(num)
# dobro(num)
# triplo(num)

# 3) Pacotes (Bibliotecas)
# Separados os módulos por pacotes/assuntos
# Exemplo 'Pacote uteis', com funções de Números, Strings, Datas, Cores.
# Cada pacote de assunto deve ser um arquivo
# Tem que ter o arquivo __init__.py (o python cria sozinho)
# Utilizar a opção de criação de diretório por: New file > Package
