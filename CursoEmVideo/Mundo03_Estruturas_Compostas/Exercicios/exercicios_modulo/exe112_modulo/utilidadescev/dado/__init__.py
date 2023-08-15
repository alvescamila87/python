def leia_dinheiro(msg):
    """
    Função verifica se a entrada de dados é uma informação numérica para ser "preço"
    :param msg: opcional, recebe a informação de preço de 'p'
    :return: retorna para 'p' caso a entrada do dado seja numérico (pode ser float) e válido
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(",", ".").strip()
        if entrada.isalpha() or entrada == "":
            print(f"\033[0;31mERRO! '{entrada}' é um preço inválido!\033[m")
        else:
            valido = True
            return float(entrada)
