# a - argumento posicional
# b - pacote de argumentos (*tupla): empacotamento / desempacotamento
# c - argumento nomeado (c="default)
# d - pacote nomeado (**dicionário{}):

def nome(a, *b):
    print(a, b)

nome('camila', 13,12,"Karoline", True, "Isabel", "Paulo", 13)


def nome2(c="default", **d):
    print(c, d)

nome2(a="não tem nada")
