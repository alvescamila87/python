# Funções: DEFs Python - PARTE 2: Tópicos a serem abordados:
# Interactive help: utilizar a função interna help() no python
# docstrings: documentação de função
# Argumentos opcionais: funções com argumentos opcionais
# Escopo de variáveis: quando variável 'nasce', 'morre', em que momentos e posições elas são visíveis, isso funciona também para importação de bibliotecas
# Retorno de resultados: retornar resultado das funções

# 1) Interactive help
# help()
# print(input.__doc__)

# 2) DocStrings 

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Gustavo Guanabara do canal CursoemVídeo.
    """
    c = i
    while c <= f:
        print(f"{c} ", end="")
        c += p
    print("FIM!")

help(contador)

