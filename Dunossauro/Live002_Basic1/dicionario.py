dicionario = {
    'chave1': ['valor1', 'valor2'],
    'chave2': ['valor3', 'valor4']
}

print(dicionario)
print(dicionario['chave2'])

pessoa = {
    'nome': 'Camila',
    'idade': 35,
    'telefones': {
        'comercial': 5168161616,
        'residencial': 634635841684,
        'celular': 935156461
    }
}

print(pessoa)
print(pessoa['telefones'])
print(pessoa['telefones']['celular'])

# funcao com dicionario

def imprime_relatorio(pessoa):
    return f"""
    Relatório parcial
    
    A colaboradora: {pessoa['nome']},
    de {pessoa['idade']} anos,
    utiliza o celular: {pessoa['telefones']['celular']}
    
    Está de férias!
    
    Ass. Diretoria
    """

print(imprime_relatorio(pessoa))

# Exercicio:

lista_numeros = list()

for valor in range(5):
    lista_numeros.append(
        int(input("Informe um valor: "))
    )

print(lista_numeros)

def quadrado(lista_de_numeros):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** 2)

    return lista_resposta


def cubo(lista_de_numeros):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** 3)

    return lista_resposta

dicionario = {
    'lista padrão': lista_numeros,
    'lista quadrada': quadrado(lista_numeros),
    'lista cúbica': cubo(lista_numeros)
}

print(dicionario)
