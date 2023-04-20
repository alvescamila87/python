from random import shuffle
a1=str(input('informe aluno 1: '))
a2=str(input('informe aluno 2: '))
a3=str(input('informe aluno 3:'))
a4=str(input('informe aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação será: {}'. format(lista))