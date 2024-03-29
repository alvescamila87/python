# Funções PARTE 2 - Exercício: Interactive helping system in Python
from time import sleep

c = ('\033[m',           # 0 - sem cor
     '\033[0;30;41m',    # 1 - vermelho
     '\033[0;30;42m',    # 2 - verde
     '\033[0;30;43m',    # 3 - amarelo
     '\033[0;30;44m',    # 4 - azul
     '\033[0;30;45m',    # 5 - roxo
     '\033[7;30m'        # 6 - branco
    );


def ajuda(com):
    titulo(f"Acessando o manual do comando '{com}'", 4)
    print(c[5], end="")
    help(com)
    print(c[0], end="")
    sleep(2)



def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end="")
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0], end="")
    sleep(1)



# Programa principal
comando = ""
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('<< ATÉ LOGO >>', 1)

