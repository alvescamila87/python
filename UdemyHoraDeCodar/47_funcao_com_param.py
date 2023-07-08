#funcao como parametro

def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

#inserindo funcao como argumento de outra:
def operacao(a, b, funcao):
    resultado = funcao(a, b)
    return resultado

a = operacao(5, 5, soma)
print(a)

b = operacao(10, 5, multiplicacao)
print(b)