# Funções PARTE 2 - Exercício: Ficha do jogador

def ficha(gols=0, nome='<desconhecido>'):
    """
    Checa quantos gols o jogador fez no campeonado.
    :param gols: opcional, recebe número de gols informados em 'n'
    :param nome: opcional, rece nome do jogador informado em 'jogador'
    :return: não há.
    Função criada no CursoEmVídeo
    """
    print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")


# Programa principal
jogador = str(input("Nome do Jogador: "))
n = str(input("Número de gols: "))
if n.isnumeric():
    n = int(n)
else:
    n = 0
if jogador.strip() == '':
    ficha(gols=n)
else:
    ficha(jogador, n)
