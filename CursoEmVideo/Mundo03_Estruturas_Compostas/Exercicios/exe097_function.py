# Função: EXERCÍCIO: Um print especial

def escreva(txt):
    tamanho = len(txt) + 4
    print("~" * tamanho)
    print(f'  {txt}')
    print("~" * tamanho)


# Programa principal
t = str(input("Digite um texto: "))
escreva(t)
