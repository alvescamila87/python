# Funções PARTE 2 - Exercício: Funções para votação

def voto(ano):
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

