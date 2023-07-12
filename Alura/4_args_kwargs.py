#arg, *args, 
def teste(arg, *args):
    print('primeiro argumento normal: {}'.format(arg))
    for arg in args:
        print('outro argumento: {}'.format(arg))

teste('python', 'é', 'muito', 'legal')

#nova opção 1
lista = ['é', 'muito', 'legal']
teste('python', *lista)

#nova opção 2
tupla = ('é', 'muito', 'legal')
teste('python', *tupla)


#**kwargs
def minha_funcao(**kwargs):
    for key, value in kwargs.items():
        print('{} = {}' .format(key, value))

minha_funcao(nome='Marlene')

#nova opção 1
dicionario = {'nome': 'malene', 'idade': 3}
minha_funcao(**dicionario)

#forma de acessar o dicionario, pela chave:
print(dicionario['nome'])
