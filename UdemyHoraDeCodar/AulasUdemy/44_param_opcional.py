#parametro opcional

#nome é o parametro setado como 'parametro opcional'/'é uma constante'
def imprime_nome(nome = "Camila"):
    print("Olá, %s" %nome)

imprime_nome()

#desconsiderando o parametro normal e pegando o da função:

imprime_nome("Karoline")
imprime_nome("Isabel")