# Módulos e Pacotes - Exercício: Formatando moedas em python

def metade(preco=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe a metado do preço informado.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço pela metade (preço / 2) NÃO formatado (quando formatado = False) ou retorna o calculo de preço pela metade formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco / 2
    return resultado if not formatacao else moeda(resultado)

def dobro(preco=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe o dobro do preço informado.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço dobrado NÃO formatado (quando formatado = False) ou retorna o calculo de preço dobrado formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco * 2
    return resultado if not formatacao else moeda(resultado)


def aumentar(preco=0, taxa=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe o aumento do preço de acordo com a taxa informada.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param taxa: opcional, recebe a informação de taxa (percentual) a ser utilizado para calcular o aumento de preço
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço com aumento, de acordo com a taxa, NÃO formatado (quando formatado = False) ou retorna o calculo de preço com aumento, de acordo com a taxa,formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco + (preco * taxa / 100)
    return resultado if formatacao is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe a diminuição do preço de acordo com a taxa informada.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param taxa: opcional, recebe a informação de taxa (percentual) a ser utilizado para calcular a diminuição de preço
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço reduzido, de acordo com a taxa, NÃO formatado (quando formatado = False) ou retorna o calculo de preço reduzido, de acordo com a taxa,formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco - (preco * taxa / 100)
    return resultado if formatacao is False else moeda(resultado)


def moeda(preco=0, moeda="R$"):
    """
    Função que inclui a formatação de moeda BRL e substitui a formatação de pontos (padrão EN) para vírgulas(padrão PT-BR)
    :param preco: opcional, recebe a informação de preço de 'p'
    :param moeda: opcional, recebe a formatação da moeda BRL
    :return: retorna as formatações de: moeda para BRL e substituição de pontos (padrão EN) para vírgulas(padrão PT-BR), com duas casas decimais após a vírgula.
    """
    return f"{moeda}{preco:.2f}".replace(".", ",")

