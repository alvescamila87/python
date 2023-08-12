# Funções PARTE 2 - Exercício: Funções para votação

def voto(ano):
    """
    -> Checa o ano de nascimento recebido versus a data atual e retorna se o voto é: opcional, obrigatório ou ainda não vota.
    :param ano: recebe o ano de nascimento da pessoa votante
    :return: retorna valor literal, ou seja, se a idade possui voto: opcional, obrigatório ou não vota
    Função criada no CursoEmVídeo (Guanabara)
    """
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif idade <= 16 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."


# Programa principal
nasc = int(input("Informe o ano de nascimento: "))
print((voto(nasc)))

