def metade(preco=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe a metado do preço informado.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço pela metade (preço / 2) NÃO formatado (quando formatado = False) ou retorna o
    calculo de preço pela metade formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco / 2
    return resultado if not formatacao else moeda(resultado)

def dobro(preco=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe o dobro do preço informado.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço dobrado NÃO formatado (quando formatado = False) ou retorna o calculo de
    preço dobrado formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco * 2
    return resultado if not formatacao else moeda(resultado)


def aumentar(preco=0, taxa=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe o aumento do preço de acordo com a taxa informada.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param taxa: opcional, recebe a informação de taxa (percentual) a ser utilizada para incidir sobre o valor do
    cálculo de aumento de preço
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço com aumento, de acordo com a taxa, NÃO formatado (quando formatado = False) ou
    retorna o calculo de preço com aumento, de acordo com a taxa,formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco + (preco * taxa / 100)
    return resultado if formatacao is False else moeda(resultado)


def diminuir(preco=0, taxa=0, formatacao=False):
    """
    -> Função que exibe calcula e exibe a diminuição do preço de acordo com a taxa informada.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param taxa: opcional, recebe a informação de taxa (percentual) a ser utilizada para incidir sobre o valor do
    cálculo de redução de preço
    :param formatacao: preco: opcional, recebe a informação se o preço deve ou não ser formatado com a função 'moeda'
    :return: retorna o calculo de preço reduzido, de acordo com a taxa, NÃO formatado (quando formatado = False) ou
    retorna o calculo de preço reduzido, de acordo com a taxa,formatado (quando formatado = True)
    Função criada no CursoEmVídeo (Guanabara)
    """
    resultado = preco - (preco * taxa / 100)
    return resultado if formatacao is False else moeda(resultado)


def moeda(preco=0, moeda="R$"):
    """
    Função que inclui a formatação de moeda BRL e substitui a formatação de pontos (padrão EN) para vírgulas
    (padrão PT-BR)
    :param preco: opcional, recebe o preço calculado/informado.
    :param moeda: opcional, recebe a formatação da moeda BRL
    :return: retorna as formatações de: moeda para BRL e substituição de pontos (padrão EN) para vírgulas(padrão PT-BR),
    com duas casas decimais após a vírgula.
    """
    return f"{moeda}{preco:.2f}".replace(".", ",")


def resumo(preco: object = 0, taxa_aumento: object = 0, taxa_reducao: object = 0) -> object:
    """
    Função que recibe um resumo detalhado do preço sendo: valor normal, metade do valor, valor dobrado, aumento
    e redução de valor com formatação de moeda.
    :param preco: opcional, recebe a informação de preço de 'p'
    :param taxa_aumento: opcional, recebe a informação de taxa (percentual) a ser utilizada para incidir sobre o valor
    do cálculo de aumento de preço
    :param taxa_reducao: opcional, recebe a informação de taxa (percentual) a ser utilizada para incidir sobre o valor
    do cálculo de redução de preço
    :return: não há retorno
    Função criada no CursoEmVídeo (Guanabara)
    """
    print("-" * 30)
    print("RESUMO DO VALOR".center(30))
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(preco)}") # \t: é a tabulação para formatação do print
    print(f"Metade do preço: \t{metade(preco, formatacao=True)}")
    print(f"Dobro do preço: \t{dobro(preco, formatacao=True)}")
    print(f"{taxa_aumento}% de aumento: \t{aumentar(preco, taxa_aumento, True)}")
    print(f"{taxa_reducao}% de redução: \t{diminuir(preco, taxa_reducao, True)}")
    print("-" * 30)