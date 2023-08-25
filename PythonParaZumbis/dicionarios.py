dic = {}
dic['nome'] = 'Camila Alves'
dic['linguagem'] = 'Python JAVA JavaScript HTML CSS'.split()
print(dic)

print(dic['nome'])


# 1) Ler arquivo e contar palavras

import string

texto = open('alice.txt').read().lower()
for c in string.punctuation:
    texto = texto.replace(c, " ")

palavras = texto.split()

word_count = {}
for p in palavras:
    if p in word_count:
        word_count[p] +=1
    else:
        word_count[p] = 1

def contador(dupla):
    return dupla[1]

duplas = sorted(word_count.items(), key=contador, reverse=True)
for dupla in duplas[:20]:
    print(dupla[0], dupla[1])
