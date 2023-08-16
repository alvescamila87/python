
def linha(tamanho=42):
    return "-" * tamanho


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    for item in lista:
        print(f"\033[33m{c}\033[m - \033[34m{item}\033[m")
        c +=1
    print(linha())
    opc = leia_int(f"\033[32mSua opção: \033[m")
    return opc

def leia_int(opcao):
    while True:
        try:
            entrada_inteiro = int(input(opcao))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Favor digitar um número inteiro válido.\033[m")
            continue
        except KeyboardInterrupt:
            print(f"\033[31mERRO: Entrada de dados interrompida pelo usuário.\033[m")
            return 0
        else:
            return entrada_inteiro