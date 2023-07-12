def dados(nome, idade=None):
    print("Nome: {}" .format(nome))
    if idade is not None:
        print("Idade: {} anos".format(idade))
    else:
        print("Idade não informada")

dados("Camila", 35)
dados("Camila")
dados(35)