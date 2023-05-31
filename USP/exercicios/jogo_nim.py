#jogo nim

#Escolha de tipo de partida
def main():
    print("Bem vindo ao jogo do NIM! Escolha: ")
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")

    escolha = int(input("O que você escolhe? "))
    while escolha != 1 and escolha != 2:
        print("Número inválido. Informe 1 ou 2 para iniciar o jogo.")
        escolha = int(input("O que você escolhe? "))

    if escolha == 1:
        print("Você escolheu iniciar uma partida isolada! ")
        partida()
    else:
        print("Você escolheu jogar um campeonato")
        campeonato()

#Computador inicia a jogada
def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        if n % (m + 1) > 0:
            return n % (m + 1)
        return m

#Usuário inicia a jogada
def usuario_escolhe_jogada(n, m):
    valor = int(input("Quantas peças você deseja retirar? "))
    while valor > m or valor <= 0 or valor > n:
        print("Oops! Jogada inválida! Tente novamente...")
        valor = int(input("Quantas peças você deseja retirar? "))

    return valor

# n = número de peças
# m = número máximo de peças a serem retiradas a cada jogada
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    while m < 1:
        print("A quantidade de peças por jogadas devem ser menor ou igual as peças totais.")
        m = int(input("Limite de peças por jogada? "))

    valor = 0
    jogada = 0
    if (n % (m + 1)) == 0:
        print("Você começa!")
        jogada = 1 #vez do usuário iniciar a partida
        while n > 0:
            if jogada == 1:
                valor = usuario_escolhe_jogada(n, m)
                print("Você tirou {} peças no tabuleiro.".format(valor))
                n = n  - valor
                print("Agora restam {} peças no tabuleiro.".format(n))
                jogada = 2
            else:
                valor = computador_escolhe_jogada(n, m)
                print("O computador tirou {} peças no tabuleiro.".format(valor))
                n = n  - valor
                print("Agora restam {} peças no tabuleiro.".format(n))
                jogada = 1

        if jogada == 1:
            print("Fim do jogo! O computador venceu =(")
            return 2 #Ponto para o computador
        else:
            print("Fim do jogo! Você venceu!!! =D")
            return 1 #Ponto para o usuário

    else:
        print("Computador começa!")
        jogada = 2 #Vez do computador iniciar a partida
        while n > 0:
            if jogada == 1:
                valor = computador_escolhe_jogada(n, m)
                print("O computador tirou {} peças no tabulero.".format(valor))
                n = n - valor
                print("Agora restam {} peças no tabuleiro.".format(n))
                jogada = 1
            else:
                valor = usuario_escolhe_jogada(n, m)
                print("Você tirou {} peças no tabuleiro.".format(valor))
                n = n - valor
                print("Agora restam {} peças no tabuleiro.".format(n))
                jogada = 2

        if jogada == 1:
            print("Fim de jogo! O computador venceu =(")
            return 2 #Ponto para o computador
        else:
            print("Fimd e jogo! Você venceu!!! =D")
            return 1 #Ponto para o usuário

def campeonato():
    quantidade_partida = 1
    placar_computador = placar_usuario = 0

    while quantidade_partida < 4:
        print("Rodada {}".format(quantidade_partida))
        if partida() == 1:
            placar_usuario = placar_computador + 1
        else:
            placar_computador = placar_computador + 1
        quantidade_partida = quantidade_partida + 1

    print("Final do campeonato!")
    print("Placar: Você {}, Computador {}".format(placar_usuario, placar_computador))

main()
