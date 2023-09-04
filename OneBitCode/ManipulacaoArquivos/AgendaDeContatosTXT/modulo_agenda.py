from agenda import *

def executar_agenda_contatos():
    while True:
        menu(['Adicionar contatos',
              'Visualizar contatos',
              'Deletar contatos',
              'Sair do programa'])

        opcao = int(input("Digite uma opção do menu: \n"))

        if opcao == 1:
            adicionar_contatos()
        elif opcao == 2:
            visualizar_contatos()
        elif opcao == 3:
            deletar_contatos()
        elif opcao == 4:
            break
        else:
            print("[ERRO] Opção inválida! Tente novamente.")

executar_agenda_contatos()