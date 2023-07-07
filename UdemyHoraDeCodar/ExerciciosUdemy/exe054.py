#funcao calcula numero e retorna média da lista

lista = [2,3,645,8,9,58,93,74,82]


def calc_media(lista):

    i = 0
    soma_numeros = 0

    while i <len(lista):
        soma_numeros = soma_numeros + lista[i]
        i = i + 1

    media_numeros = soma_numeros / len(lista)
    
    return media_numeros

media_numeros_2 = calc_media(lista)

print(media_numeros_2)

#outra forma de resulver a funcao

def calc_media_2(lista):
    media = 0

    soma = 0

    for n in lista:
        soma += n
    
    media = soma / len(lista)

    return media

media_numeros_3 = calc_media_2(lista)

print(media_numeros_3)