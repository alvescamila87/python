# Funções #5 - Documentando funções com docstrings
# PEP-257
# TODO: Comentários para TO-DO.
def soma(x, y):
    """
    Soma 2 tipos somáveis.
    :param x: objeto somável
    :param y: objeto somável
    :return: soma de dois somáveis.
    NOTE: Função foi documentada.
    TODO: Melhorar a docstring.
    """
    return x + y

print("soma: ", soma(1,2))
print(soma.__doc__)
