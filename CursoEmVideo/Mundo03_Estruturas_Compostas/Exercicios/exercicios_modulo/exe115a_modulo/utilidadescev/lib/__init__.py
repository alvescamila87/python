
def linha(txt):
    tamanho = len(txt) + 5
    print("-" * tamanho)
    print(f"  {txt}")
    print("-" * tamanho)


def menu():
    while True:
        linha(txt = "           MENU PRINCIPAL          ")
        print(f"1 - Ver pessoas cadastradas")
        print(f"2 - Cadastrar nova Pessoa")
        print(f"3 - Sair do sistema")
        print(f"-" * 40)
        try:
            comando = ""
            comando = int(input("Informe a sua opção: "))
        except (ValueError, TypeError):
            print(f"\033[31mERRO: Favor digitar um número inteiro válido.\033[m")
            continue
        if comando not in range(1,4):
            print(f"\033[31mERRO: Digite uma opção válida!\033[m")
        if comando in range(1,3):
            linha(txt=f"               Opção {comando}              ")
        if comando == 3:
            break
    linha(txt=f"        Saindo do sistema... Até logo!      ")

