#manipulação de strings: trocando / substituindo palavra em string

frase = "O rato roeu a roupa do rei de Roma"

#substituir
print(frase.replace("rato", "leão"))

frase2 = "Vou testar o replace em duas palavras testar"

#substituir um dos 'testar' da frase
print(frase2.replace("testar", "trocou", 1))
